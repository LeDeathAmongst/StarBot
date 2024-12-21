"""Module for the UpdateRed cog."""
import asyncio
import asyncio.subprocess
import io
import logging
import pathlib
import re
import sys
import tarfile
import time
from typing import ClassVar, Iterable, List, Optional, Pattern, Tuple

from Star-Utils import Cog

import discord
from starbot.core import checks, commands, Config

log = logging.getLogger("starbot.updatered")


class UpdateBot(getattr(commands, "Cog", object)):
    """Update Red from Discord.

    To get the most out of this cog, run red with systemd or pm2 on
    Linux, or the launcher on Windows, then use the `[p]restart`
    command to restart the bot after updating.
    """

    DEV_LINK: ClassVar[str] = (
        "https://github.com/Cog-Creators/StarBot/tarball/"
        "V3/develop#egg=StarBot"
    )
    IS_VENV: ClassVar[bool] = hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )
    PIP_INSTALL_ARGS: ClassVar[Tuple[str, ...]] = (
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "--force-reinstall",
    )
    if not IS_VENV:
        PIP_INSTALL_ARGS += ("--user",)
    _BIN_PATH: ClassVar[pathlib.Path] = pathlib.Path(sys.executable).parent
    _WINDOWS_BINARIES: ClassVar[List[pathlib.Path]] = [
        _BIN_PATH / "starbot.exe",
        _BIN_PATH / "starbot-launcher.exe",
        *pathlib.Path(discord.__file__).parent.glob("bin/*.dll"),
    ]
    _SAVED_PKG_RE: ClassVar[Pattern[str]] = re.compile(r"\s+Saved\s(?P<path>.*)$")

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=0x12345678, force_registration=True)
        self.config.register_global(fork_url=None)

    @checks.is_owner()
    @commands.command(aliases=["botupd"])
    async def update(
        self, ctx: commands.Context, version: str = "stable", *extras: str
    ) -> None:
        """Update Red with pip.

        The optional `version` argument can be set to any one of the
        following:
         - `stable` (default) - Update to the latest release on PyPI.
         - `pre` - Update to the latest pre-release, if available.
         - `dev` - Update from source control, i.e. V3/develop on
         GitHub.
         - Any specific version, e.g. `3.0.0b19`.

        You may also specify any number of `extras`, which are extra
        requirements you wish to install with Red. For example, to
        update mongo requirements with Red, run the command with
        `[p]update <version> mongo`.

        Please note that when specifying any invalid arguments, the cog
        will naively try to run the update command with those arguments,
        possibly resulting in a misleading error message.
        """
        version = version.lower()
        pre = False
        dev = False
        if version == "stable":
            version_marker = ""
        elif version == "pre":
            pre = True
            version_marker = ""
        elif version == "dev":
            dev = True
            version_marker = ""
        else:
            version_marker = "==" + version

        await self._update_and_communicate(
            ctx, version_marker=version_marker, pre=pre, dev=dev, extras=extras
        )

    @checks.is_owner()
    @commands.command()
    async def urlupdate(self, ctx: commands.Context, *, url: str) -> None:
        """Update [botname] directly from a pip-installable URL."""
        try:
            await self._update_and_communicate(ctx, url=url)
        except tarfile.ReadError:
            await ctx.send("That link does not appear to point to a tarball.")

    @checks.is_owner()
    @commands.command(name="setforkurl")
    async def setforkurl(self, ctx: commands.Context, repo_url: str) -> None:
        """Set the URL for the fork to be used with forkupdate.

        Arguments:
        - `repo_url`: The Git repository URL in the form `git+https://github.com/owner/repo`.
        """
        if not repo_url.startswith("git+https://github.com/"):
            await ctx.send("Please provide a valid Git repository URL.")
            return

        await self.config.fork_url.set(repo_url)
        await ctx.send(f"Fork URL set to: {repo_url}")

    @checks.is_owner()
    @commands.command(name="forkupdate", aliases=["fupd", "updf"])
    async def forkupdate(self, ctx: commands.Context) -> None:
        """Update the bot using the stored fork URL."""
        repo_url = await self.config.fork_url()
        if not repo_url:
            await ctx.send("No fork URL set. Please set one using `setforkurl`.")
            return

        await self._update_and_communicate(ctx, url=repo_url)

    async def _update_and_communicate(
        self,
        ctx: commands.Context,
        *,
        url: Optional[str] = None,
        version_marker: str = "",
        pre: bool = False,
        dev: bool = False,
        extras: Optional[Iterable[str]] = None,
    ) -> None:
        async with ctx.typing():
            return_code, stdout = await self.update_red(
                url=url, version_marker=version_marker, pre=pre, dev=dev, extras=extras
            )

        if return_code:
            msg = "Something went wrong whilst updating."
        else:
            msg = "Update successful. Restarting your bot is recommended."

        if stdout:
            prompt = await ctx.send(
                msg + " Would you like to see the console output? (y/n)"
            )

            try:
                response: Optional[discord.Message] = await ctx.bot.wait_for(
                    "message",
                    check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                    timeout=15.0,
                )
            except asyncio.TimeoutError:
                response = None

            if response and response.content.lower() in ("y", "yes"):
                with io.BytesIO(stdout.encode()) as fp:
                    cur_date = time.strftime("%Y-%m-%dT%H-%M-%S")
                    await ctx.send(
                        file=discord.File(fp, filename=f"updatered-{cur_date}.log")
                    )
            else:
                await prompt.edit(content=msg)
        else:
            await ctx.send(msg)

    async def update_red(
        self,
        *,
        url: Optional[str] = None,
        version_marker: str = "",
        pre: bool = False,
        dev: bool = False,
        extras: Optional[Iterable[str]] = None,
    ) -> Tuple[int, str]:
        """Update the bot.

        Returns
        -------
        Tuple[int, str]
            A tuple in the form (return_code, stdout).

        """
        if extras:
            extras_str = f"[{','.join(extras)}]"
        else:
            extras_str = ""

        if dev:
            package = self.DEV_LINK + extras_str
        elif url is not None:
            package = url
        else:
            package = "StarBot" + extras_str + version_marker

        args = self.PIP_INSTALL_ARGS + (package,)

        if pre:
            args += ("--pre",)

        if sys.platform == "win32":
            # If we try to update whilst running Red, Windows will throw a permission
            # error due to binaries being in use (apparently).
            self.rename_executables()

        log.debug("Installing Red package with command: %s", " ".join(args))

        process: Optional[asyncio.subprocess.Process] = None
        stdout = ""
        try:
            process = await asyncio.create_subprocess_exec(
                *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
            )

            stdout_data = (await process.communicate())[0]
            if stdout_data is not None:
                stdout += "\n" + stdout_data.decode()
        finally:
            if sys.platform == "win32" and process and process.returncode:
                self.rename_executables(undo=True)

        return process.returncode, stdout

    @classmethod
    def rename_executables(cls, *, undo: bool = False) -> None:
        """This is a helper method for renaming Red's executables in Windows."""
        for exe in cls._WINDOWS_BINARIES:
            exe_old = exe.with_suffix(".old")
            if undo:
                from_file, to_file = exe_old, exe
            else:
                from_file, to_file = exe, exe_old

            if not from_file.is_file():
                continue
            log.debug("Renaming %s to %s...", from_file, to_file)
            try:
                from_file.rename(to_file)
            except OSError:
                log.error("Failed to rename %s to %s!", from_file, to_file)

    @classmethod
    def cleanup_old_executables(cls) -> None:
        for exe in cls._WINDOWS_BINARIES:
            old_exe = exe.with_suffix(".old")
            if not old_exe.is_file():
                continue
            log.debug("Deleting old file %s...", old_exe)
            try:
                old_exe.unlink()
            except OSError:
                log.debug("Failed to delete old file %s!", old_exe)
