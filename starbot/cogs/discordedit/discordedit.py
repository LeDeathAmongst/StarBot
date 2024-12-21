from Star-Utils import Cog, CogsUtils  # isort:skip
from starbot.core.bot import Red  # isort:skip
from starbot.core.i18n import Translator, cog_i18n  # isort:skip
import typing  # isort:skip

# from .editautomod import EditAutoMod
from .editguild import EditGuild
from .editrole import EditRole
from .edittextchannel import EditTextChannel
from .editthread import EditThread
from .editvoicechannel import EditVoiceChannel

# Credits:
# General repo credits.

_: Translator = Translator("DiscordEdit", __file__)

BASES = [EditGuild, EditRole, EditTextChannel, EditThread, EditVoiceChannel]  # EditAutoMod


@cog_i18n(_)
class DiscordEdit(*BASES, Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
        self.logs = CogsUtils.get_logger("DiscordEdit")
    """A cog to edit Discord default objects, like guilds, roles, text channels, voice channels, threads and AutoMod!"""

    async def red_delete_data_for_user(self, *args, **kwargs) -> None:
        """Nothing to delete."""
        return

    async def red_get_data_for_user(self, *args, **kwargs) -> typing.Dict[str, typing.Any]:
        """Nothing to get."""
        return {}
