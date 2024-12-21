from starbot.core import Config

config: Config = Config.get_conf(None, identifier=481923957134912, cog_name="Aurora")


def register_config(config_obj: Config):
    config_obj.register_guild(
        show_moderator=True,
        use_discord_permissions=True,
        respect_hierarchy=True,
        ignore_modlog=True,
        ignore_other_bots=True,
        dm_users=True,
        log_channel=" ",
        immune_roles=[],
        history_ephemeral=False,
        history_inline=False,
        history_pagesize=5,
        history_inline_pagesize=6,
        auto_evidenceformat=False,
        addrole_whitelist=[],
    )
    config_obj.register_user(
        history_ephemeral=None,
        history_inline=None,
        history_pagesize=None,
        history_inline_pagesize=None,
        auto_evidenceformat=None,
    )
