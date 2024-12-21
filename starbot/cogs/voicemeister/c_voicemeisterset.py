import discord
from starbot.core import commands, checks
from starbot.core.utils.chat_formatting import success, error, warning, info
from Star-Utils import Cog

class VoiceMeisterSet(Cog):
    """Configure the VoiceMeister cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.voicemeister_cog = bot.get_cog("VoiceMeister")

    @commands.group(aliases=["vmset"])
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    async def voicemeisterset(self, ctx: commands.Context) -> None:
        """Configure the VoiceMeister cog."""

    @voicemeisterset.command()
    async def settings(self, ctx: commands.Context) -> None:
        """Display current settings."""
        if not ctx.guild:
            return
        server_section = SettingDisplay("Server Settings")
        server_section.add(
            "Admin access all VoiceMeisters",
            await self.voicemeister_cog.config.guild(ctx.guild).admin_access(),
        )
        server_section.add(
            "Moderator access all VoiceMeisters",
            await self.voicemeister_cog.config.guild(ctx.guild).mod_access(),
        )
        bot_roles = ", ".join(
            [role.name for role in await self.voicemeister_cog.get_bot_roles(ctx.guild)]
        )
        if bot_roles:
            server_section.add("Bot roles allowed in all VoiceMeisters", bot_roles)

        voicemeister_sections = []
        avcs = await self.voicemeister_cog.get_all_voicemeister_source_configs(ctx.guild)
        for avc_id, avc_settings in avcs.items():
            source_channel = ctx.guild.get_channel(avc_id)
            if not isinstance(source_channel, discord.VoiceChannel):
                continue
            dest_category = ctx.guild.get_channel(avc_settings["dest_category_id"])
            voicemeister_section = SettingDisplay(f"VoiceMeister - {source_channel.name}")
            voicemeister_section.add(
                "Room type",
                avc_settings["room_type"].capitalize(),
            )
            voicemeister_section.add(
                "Destination category",
                f"#{dest_category.name}" if dest_category else "INVALID CATEGORY",
            )
            if avc_settings["legacy_text_channel"]:
                voicemeister_section.add(
                    "Legacy Text Channel",
                    "True",
                )
            if not avc_settings["perm_send_messages"]:
                voicemeister_section.add(
                    "Send Messages",
                    "False",
                )
            if not avc_settings["perm_owner_manage_channels"]:
                voicemeister_section.add(
                    "Owner Manage Channel",
                    "False",
                )
            member_roles = self.voicemeister_cog.get_member_roles(source_channel)
            if member_roles:
                voicemeister_section.add(
                    "Member Roles" if len(member_roles) > 1 else "Member Role",
                    ", ".join(role.name for role in member_roles),
                )
            room_name_format = "Username"
            if avc_settings["channel_name_type"] in channel_name_template:
                room_name_format = avc_settings["channel_name_type"].capitalize()
            elif (
                avc_settings["channel_name_type"] == "custom"
                and avc_settings["channel_name_format"]
            ):
                room_name_format = f'Custom: "{avc_settings["channel_name_format"]}"'
            voicemeister_section.add("Room name format", room_name_format)
            voicemeister_sections.append(voicemeister_section)

        message = server_section.display(*voicemeister_sections)
        required_check, optional_check, _ = await self._check_all_perms(ctx.guild)
        if not required_check:
            message += "\n" + error(
                "It looks like I am missing one or more required permissions. "
                "Until I have them, the VoiceMeister cog may not function properly "
                "for all VoiceMeister Sources. "
                "Check `[p]voicemeisterset permissions` for more information."
            )
        elif not optional_check:
            message += "\n" + warning(
                "All VoiceMeisters will work correctly, as I have all of the required permissions. "
                "However, it looks like I am missing one or more optional permissions "
                "for one or more VoiceMeisters. "
                "Check `[p]voicemeisterset permissions` for more information."
            )
        await ctx.send(message)

    @voicemeisterset.command(aliases=["perms"])
    async def permissions(self, ctx: commands.Context) -> None:
        """Check that the bot has all needed permissions."""
        if not ctx.guild:
            return
        required_check, optional_check, details_list = await self._check_all_perms(
            ctx.guild, detailed=True
        )
        if not details_list:
            await ctx.send(
                info(
                    "You don't have any VoiceMeister Sources set up! "
                    "Set one up with `[p]voicemeisterset create` first, "
                    "then I can check what permissions I need for it."
                )
            )
            return

        if (
            len(details_list) > 1
            and not ctx.channel.permissions_for(ctx.guild.me).add_reactions
        ):
            await ctx.send(
                error(
                    "Since you have multiple VoiceMeister Sources, "
                    'I need the "Add Reactions" permission to display permission information.'
                )
            )
            return

        if not required_check:
            await ctx.send(
                error(
                    "It looks like I am missing one or more required permissions. "
                    "Until I have them, the VoiceMeister Source(s) in question will not function properly."
                    "\n\n"
                    "The easiest way of fixing this is just giving me these permissions as part of my server role, "
                    "otherwise you will need to give me these permissions on the VoiceMeister Source and destination "
                    "category, as specified below."
                )
            )
        elif not optional_check:
            await ctx.send(
                warning(
                    "It looks like I am missing one or more optional permissions. "
                    "All VoiceMeisters will work, however some extra features may not work. "
                    "\n\n"
                    "The easiest way of fixing this is just giving me these permissions as part of my server role, "
                    "otherwise you will need to give me these permissions on the destination category, "
                    "as specified below."
                    "\n\n"
                    "In the case of optional permissions, any permission on the VoiceMeister Source will be copied to "
                    "the created VoiceMeister, as if we were cloning the VoiceMeister Source. In order for this to work, "
                    "I need each permission to be allowed in the destination category (or server). "
                    "If it isn't allowed, I will skip copying that permission over."
                )
            )
        else:
            await ctx.send(success("Everything looks good here!"))

        if len(details_list) > 1:
            if (
                ctx.channel.permissions_for(ctx.guild.me).add_reactions
                and ctx.channel.permissions_for(ctx.guild.me).read_message_history
            ):
                await menu(ctx, details_list, DEFAULT_CONTROLS, timeout=60.0)
            else:
                for details in details_list:
                    await ctx.send(details)
        else:
            await ctx.send(details_list[0])

    async def _check_all_perms(
        self, guild: discord.Guild, *, detailed: bool = False
    ) -> tuple[bool, bool, list[str]]:
        """Check all permissions for all VoiceMeisters in a guild."""
        result_required = True
        result_optional = True
        result_list = []
        avcs = await self.voicemeister_cog.get_all_voicemeister_source_configs(guild)
        for avc_id, avc_settings in avcs.items():
            voicemeister_source = guild.get_channel(avc_id)
            category_dest = guild.get_channel(avc_settings["dest_category_id"])
            if isinstance(voicemeister_source, discord.VoiceChannel) and isinstance(
                category_dest, discord.CategoryChannel
            ):
                (
                    required_check,
                    optional_check,
                    detail,
                ) = self.voicemeister_cog.check_perms_source_dest(
                    voicemeister_source,
                    category_dest,
                    with_manage_roles_guild=avc_settings["room_type"] != "server",
                    with_legacy_text_channel=avc_settings["legacy_text_channel"],
                    with_optional_clone_perms=True,
                    detailed=detailed,
                )
                result_required = result_required and required_check
                result_optional = result_optional and optional_check
                if detailed:
                    result_list.append(detail)
                elif not result_required and not result_optional:
                    break
        return result_required, result_optional, result_list
