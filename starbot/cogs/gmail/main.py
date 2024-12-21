import asyncio
import logging

from starbot.core import Config, commands
from starbot.core.bot import Red

from .abc import CompositeMetaClass
from .commands import Commands
from .common.models import DB

log = logging.getLogger("red.vrt.gmail")


class Gmail(Commands, commands.Cog, metaclass=CompositeMetaClass):
    """
    Send emails using your Gmail account.

    Use `[p]gmailhelp` for help getting started.
    """

    def __init__(self, bot: Red):
        super().__init__()
        self.bot: Red = bot
        self.config = Config.get_conf(self, 117, force_registration=True)
        self.config.register_global(db={})

        self.db: DB = DB()
        self.saving = False

    async def red_delete_data_for_user(self, *, requester: str, user_id: int):
        if requester == "owner" and user_id == self.bot.owner_id:
            # Wipe config
            self.db = DB()
            await self.save()

    async def red_get_data_for_user(self, *, user_id: int):
        return

    async def cog_load(self) -> None:
        asyncio.create_task(self.initialize())

    async def initialize(self) -> None:
        await self.bot.wait_until_red_ready()
        data = await self.config.db()
        self.db = await asyncio.to_thread(DB.model_validate, data)
        log.info("Config loaded")

    async def save(self) -> None:
        if self.saving:
            return
        try:
            self.saving = True
            dump = await asyncio.to_thread(self.db.model_dump)
            await self.config.db.set(dump)
        except Exception as e:
            log.exception("Failed to save config", exc_info=e)
        finally:
            self.saving = False
