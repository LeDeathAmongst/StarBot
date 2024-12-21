.. _minecraft:
=========
Minecraft
=========

This is the cog guide for the ``Minecraft`` cog. This guide contains the collection of commands which you can use in the cog.
Through this guide, ``[p]`` will always represent your prefix. Replace ``[p]`` with your own prefix when you use these commands in Discord.

.. note::

    Ensure that you are up to date by running ``[p]cog update minecraft``.
    If there is something missing, or something that needs improving in this documentation, feel free to create an issue `here <https://github.com/LeDeathAmongst/StarCogs/issues>`_.
    This documentation is generated everytime this cog receives an update.

---------------
About this cog:
---------------

A cog to display informations about Minecraft Java users and servers, and notify for each change of a server!

---------
Commands:
---------

Here are all the commands included in this cog (9):

* ``[p]minecraft``
 Get informations about Minecraft Java.

* ``[p]minecraft addserver [channel] <server_url>``
 Add a Minecraft Java server in Config to get automatically new status.

* ``[p]minecraft checkplayers [channel] <state>``
 Include players joining or leaving the server in notifications.

* ``[p]minecraft editlastmessage [channel] <state>``
 Edit the last message sent for changes.

* ``[p]minecraft forcecheck``
 Force check Minecraft Java servers in Config.

* ``[p]minecraft getdebugloopsstatus``
 Get an embed for check loop status.

* ``[p]minecraft getplayerskin <player> [overlay=False]``
 Get Minecraft Java player skin by name.

* ``[p]minecraft getserver <server_url>``
 Get informations about a Minecraft Java server.

* ``[p]minecraft removeserver [channel] <server_url>``
 Remove a Minecraft Java server in Config.

------------
Installation
------------

If you haven't added my repo before, lets add it first. We'll call it "StarCogs" here.

.. code-block:: ini

    [p]repo add StarCogs https://github.com/LeDeathAmongst/StarCogs

Now, we can install Minecraft.

.. code-block:: ini

    [p]cog install StarCogs minecraft

Once it's installed, it is not loaded by default. Load it by running the following command:

.. code-block:: ini

    [p]load minecraft

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