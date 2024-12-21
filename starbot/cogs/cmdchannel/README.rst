.. _cmdchannel:
==========
CmdChannel
==========

This is the cog guide for the ``CmdChannel`` cog. This guide contains the collection of commands which you can use in the cog.
Through this guide, ``[p]`` will always represent your prefix. Replace ``[p]`` with your own prefix when you use these commands in Discord.

.. note::

    Ensure that you are up to date by running ``[p]cog update cmdchannel``.
    If there is something missing, or something that needs improving in this documentation, feel free to create an issue `here <https://github.com/LeDeathAmongst/StarCogs/issues>`_.
    This documentation is generated everytime this cog receives an update.

---------------
About this cog:
---------------

A cog to send the result of a command to another channel!

---------
Commands:
---------

Here are all the commands included in this cog (5):

* ``[p]cmdchannel <channel> <command>``
 Use `[p]cmdchannel`, `[p]cmduser` and `[p]cmduserchannel`.

* ``[p]cmdchannel channel <channel> <command>``
 Act as if the command had been typed in the channel of your choice.

* ``[p]cmdchannel testvar``
 Test variables.

* ``[p]cmdchannel user <user> <command>``
 Act as if the command had been typed by imitating the specified user.

* ``[p]cmdchannel userchannel <user> [channel] <command>``
 Act as if the command had been typed in the channel of your choice by imitating the specified user.

------------
Installation
------------

If you haven't added my repo before, lets add it first. We'll call it "StarCogs" here.

.. code-block:: ini

    [p]repo add StarCogs https://github.com/LeDeathAmongst/StarCogs

Now, we can install CmdChannel.

.. code-block:: ini

    [p]cog install StarCogs cmdchannel

Once it's installed, it is not loaded by default. Load it by running the following command:

.. code-block:: ini

    [p]load cmdchannel

----------------
Further Support:
----------------

Check out my docs `here <https://StarCogs.readthedocs.io/en/latest/>`_.
Mention me in the #support_other-cogs in the `cog support server <https://discord.gg/GET4DVk>`_ if you need any help.
Additionally, feel free to open an issue or pull request to this repo.

--------
Credits:
--------

Thanks to Kreusada for the Python code to automatically generate this documentation!