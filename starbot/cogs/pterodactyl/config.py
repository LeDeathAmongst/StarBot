from starbot.core import Config

config: Config = Config.get_conf(None, identifier=457581387213637448123567, cog_name="Pterodactyl", force_registration=True)

def register_config(config_obj: Config) -> None:
    config_obj.register_global(
        base_url="panel.danbot.host",
        server_id="9d863330",
        console_channel=None,
        console_commands_enabled=False,
        current_status='',
        chat_regex=r"^\[\d{2}:\d{2}:\d{2}\sINFO\]: (?!\[(?:Server|Rcon)\])(?:<|\[)(\w+)(?:>|\]) (.*)",
        server_regex=r"^\[\d{2}:\d{2}:\d{2} INFO\]:(?: \[Not Secure\])? \[(?:Server|Rcon)\] (.*)",
        join_regex=r"^\[\d{2}:\d{2}:\d{2} INFO\]: ([^<\n]+) joined the game$",
        leave_regex=r"^\[\d{2}:\d{2}:\d{2} INFO\]: ([^<\n]+) left the game$",
        achievement_regex=r"^\[\d{2}:\d{2}:\d{2} INFO\]: (.*) has (made the advancement|completed the challenge) \[(.*)\]$",
        chat_command='tellraw @a ["",{"text":".$N ","color":".$C","insertion":"<@.$I>","hoverEvent":{"action":"show_text","contents":"Shift click to mention this user inside Discord"}},{"text":"(DISCORD):","color":"blue","clickEvent":{"action":"open_url","value":".$V"},"hoverEvent":{"action":"show_text","contents":"Click to join the Discord Server"}},{"text":" .$M","color":"white"}]', # noqa: E501
        topic='Server IP: .$H\nServer Players: .$P/.$M',
        topic_hostname=None,
        topic_port=25565,
        api_endpoint="minecraft",
        chat_channel=None,
        startup_msg='Server started!',
        shutdown_msg='Server stopped!',
        join_msg='Welcome to the server! 👋',
        leave_msg='Goodbye! 👋',
        mask_ip=True,
        invite=None,
        regex_blacklist={},
    )
