================
Rapidlog utility
================

Rapidlog is simple handler for standard python logging package, and simple web agent (rapidagent) displaing
messages. Messages delivered asyncroniously over RabbitMq server. Rapidagent uses pika+Tornado loop for async messaging.


Installation
------------

::

  $ pip install rapidlog



Quick start
-----------
- Start rapidagent web server:

::

  $ rapidagent [settings file]

If you will use rapidlog handlers, you will see messages in this pages. Easier way is

::

  $ cd examples
  $ python app.py

Take a look logging configuration, and rapidagent.conf file.
