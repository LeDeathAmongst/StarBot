.. _memberprefix:
============
MemberPrefix
============

This is the cog guide for the ``MemberPrefix`` cog. This guide contains the collection of commands which you can use in the cog.
Through this guide, ``[p]`` will always represent your prefix. Replace ``[p]`` with your own prefix when you use these commands in Discord.

.. note::

    Ensure that you are up to date by running ``[p]cog update memberprefix``.
    If there is something missing, or something that needs improving in this documentation, feel free to create an issue `here <https://github.com/LeDeathAmongst/StarCogs/issues>`_.
    This documentation is generated everytime this cog receives an update.

---------------
About this cog:
---------------

A cog to allow a member to choose custom prefixes, just for them!

---------
Commands:
---------

Here are all the commands included in this cog (4):

* ``[p]memberprefix [prefixes]...``
 Sets [botname]'s prefix(es) for you only.

* ``[p]setmemberprefix``
 Configure MemberPrefix.

* ``[p]setmemberprefix purge <guild>``
 Clear all members prefixes for a specified server.

* ``[p]setmemberprefix resetmemberprefix <guild> <user>``
 Clear prefixes for a specified member in a specified server.

------------
Installation
------------

If you haven't added my repo before, lets add it first. We'll call it "StarCogs" here.

.. code-block:: ini

    [p]repo add StarCogs https://github.com/LeDeathAmongst/StarCogs

Now, we can install MemberPrefix.

.. code-block:: ini

    [p]cog install StarCogs memberprefix

Once it's installed, it is not loaded by default. Load it by running the following command:

.. code-block:: ini

    [p]load memberprefix

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