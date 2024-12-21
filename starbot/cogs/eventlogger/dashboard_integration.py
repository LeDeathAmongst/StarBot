#from starbot.core import commands  # isort:skip
#from starbot.core.bot import Red  # isort:skip


#class DashboardIntegration:
#    bot: Red

#    @Cog.listener()
#    async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
#        if hasattr(self, "settings") and hasattr(self.settings, "commands_added"):
#            await self.settings.commands_added.wait()
#        dashboard_cog.rpc.third_parties_handler.add_third_party(self)

from Star-Utils import Cog, CogsUtils
from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.i18n import Translator
import discord
import typing as t
import os

import wtforms
from starbot.core.utils.chat_formatting import humanize_list

#_: Translator = Translator("EmbedUtils", __file__)

def dashboard_page(*args, **kwargs):
    def decorator(func: t.Callable):
        func.__dashboard_decorator_params__ = (args, kwargs)
        return func
    return decorator

class DashboardIntegration(Cog):
    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config: Config = Config.get_conf(self, identifier=1234567891, force_registration=True)
        self.config.register_guild(channels={}, command_log_channel=None)
        self._registered = False

    @Cog.listener()
    async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
        if not self._registered:
            try:
                dashboard_cog.rpc.third_parties_handler.add_third_party(self)
                self._registered = True
            except RuntimeError as e:
                print(f'Failed to register third party: {e}')

    async def get_logging_configuration(self, user: discord.User, guild: discord.Guild, **kwargs) -> t.Dict[str, t.Any]:
        channels = await self.config.guild(guild).channels()
        command_log_channel_id = await self.config.guild(guild).command_log_channel()
        command_log_channel = guild.get_channel(command_log_channel_id) if command_log_channel_id else None

        # Define event categories
        event_categories = {
            'app': ['integration_create', 'integration_delete', 'integration_update'],
            'automod': ['automod_rule_create', 'automod_rule_delete', 'automod_rule_update'],
            'ban': ['member_ban', 'member_unban'],
            # Add more categories as needed
        }

        # Generate event options
        event_options = ''.join(
            f'<option value="{event}">{event.replace("_", " ").title()}</option>'
            for category in event_categories.values() for event in category
        )

        # Generate channel options
        channel_options = ''.join(
            f'<option value="{channel.id}">{channel.name}</option>'
            for channel in guild.text_channels
        )

        source = """
        <h3>Logging Configuration</h3>
        <form method="post" action="{{ request_url }}">
          <label for="event">Event:</label>
          <select id="event" name="event" required>
            {event_options}
          </select>

          <label for="channel">Channel:</label>
          <select id="channel" name="channel" required>
            {channel_options}
          </select>

          <button type="submit">Set Logging Channel</button>
        </form>
        <h3>Current Configuration</h3>
        <ul>
          {% for event, channel_id in channels.items() %}
            <li>{{ event }}: {{ guild.get_channel(channel_id).mention if guild.get_channel(channel_id) else "Unknown Channel" }}</li>
          {% endfor %}
          {% if command_log_channel %}
            <li>Command Log: {{ command_log_channel.mention }}</li>
          {% endif %}
        </ul>
        """.format(event_options=event_options, channel_options=channel_options)

        return {
            'status': 0,
            'web_content': {
                'source': source,
                'channels': channels,
                'command_log_channel': command_log_channel,
                'guild': guild,
                'request_url': kwargs['request_url']
            }
        }

    @dashboard_page(name='configure', description='Configure Event Logging', methods=('GET', 'POST'), is_owner=True)
    async def configure_logging_page(self, user: discord.User, guild: discord.Guild, **kwargs) -> t.Dict[str, t.Any]:
        if kwargs['method'] == 'POST':
            form = kwargs['data']['form']
            event = form.get('event')
            channel_id = int(form.get('channel'))
            async with self.config.guild(guild).channels() as channels:
                channels[event] = channel_id
            return {
                'status': 0,
                'notifications': [{
                    'message': f'Logging channel for {event} set to <#{channel_id}>',
                    'category': 'success'
                }],
                'redirect_url': kwargs['request_url']
            }
        return await self.get_logging_configuration(user, guild, **kwargs)
