.. _runcode:
=======
RunCode
=======

This is the cog guide for the ``RunCode`` cog. This guide contains the collection of commands which you can use in the cog.
Through this guide, ``[p]`` will always represent your prefix. Replace ``[p]`` with your own prefix when you use these commands in Discord.

.. note::

    Ensure that you are up to date by running ``[p]cog update runcode``.
    If there is something missing, or something that needs improving in this documentation, feel free to create an issue `here <https://github.com/LeDeathAmongst/StarCogs/issues>`_.
    This documentation is generated everytime this cog receives an update.

---------------
About this cog:
---------------

A cog to compile and run codes in some languages! Use `[p]setruncode listlanguages` to get a list of all the available languages.

---------
Commands:
---------

Here are all the commands included in this cog (7):

* ``[p]runcode [verbose=False] [language] [parameters] [code]``
 Run a code in a langage, with Wandbox API.

* ``[p]runtio [verbose] <language> [parameters] [code]``
 Run a code in a langage, with Tio API.

* ``[p]setruncode``
 View RunCode options.

* ``[p]setruncode listengines <language>``
 Shows a list of all the available engines for a specified language, only for Wandbox API.

* ``[p]setruncode listextensions``
 Lists all the languages extensions.

* ``[p]setruncode listidentifiers``
 Lists all the languages identifiers recognized by the bot, only for Wandbox API.

* ``[p]setruncode listlanguages <"wandbox"|"tio">``
 Shows a list of all the available languages, or Wandbox or Tio API.

------------
Installation
------------

If you haven't added my repo before, lets add it first. We'll call it "StarCogs" here.

.. code-block:: ini

    [p]repo add StarCogs https://github.com/LeDeathAmongst/StarCogs

Now, we can install RunCode.

.. code-block:: ini

    [p]cog install StarCogs runcode

Once it's installed, it is not loaded by default. Load it by running the following command:

.. code-block:: ini

    [p]load runcode

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