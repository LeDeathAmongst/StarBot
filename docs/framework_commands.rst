.. red commands module documentation

================
Commands Package
================

This package acts almost identically to :doc:`discord.ext.commands <dpy:ext/commands/api>`; i.e.
all of the attributes from discord.py's are also in ours. 
Some of these attributes, however, have been slightly modified, while others have been added to
extend functionalities used throughout the bot, as outlined below.

.. autofunction:: starbot.core.commands.command

.. autofunction:: starbot.core.commands.hybrid_command

.. autofunction:: starbot.core.commands.group

.. autofunction:: starbot.core.commands.hybrid_group

.. autoclass:: starbot.core.commands.Cog

    .. automethod:: format_help_for_context
    
    .. automethod:: red_get_data_for_user
    
    .. automethod:: red_delete_data_for_user

.. autoclass:: starbot.core.commands.GroupCog

.. autoclass:: starbot.core.commands.Command
    :members:
    :inherited-members: format_help_for_context

.. autoclass:: starbot.core.commands.HybridCommand
    :members:

.. autoclass:: starbot.core.commands.Group
    :members:

.. autoclass:: starbot.core.commands.HybridGroup
    :members:

.. autoclass:: starbot.core.commands.Context
    :members:

.. autoclass:: starbot.core.commands.GuildContext

.. autoclass:: starbot.core.commands.DMContext

.. autoclass:: starbot.core.commands.UserFeedbackCheckFailure
    :members:

.. automodule:: starbot.core.commands.requires
    :members: PrivilegeLevel, PermState, Requires

.. automodule:: starbot.core.commands.converter
    :members:
    :exclude-members: UserInputOptional, convert
    :no-undoc-members:

    .. autodata:: UserInputOptional
        :annotation:

.. _framework-commands-help:

******************
Help Functionality
******************

.. warning::

    The content in this section is `provisional <developer-guarantees-exclusions>` and may change
    without prior notice or warning. Updates to this will be communicated
    on `this issue <https://github.com/Cog-Creators/StarBot/issues/4084>`_


.. automodule:: starbot.core.commands.help
    :members:
