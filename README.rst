================
Rapidlog utility
================

Rapid log is special handler for python logging
module, uses RabbitMq as transport layer. For displaing
messages it uses Tornado+Pika application, and websockets
layer for delivering messages.

Install requirements
--------------------
We strongly recommend use virtualenv. For installing env,
please use:
::

$ pip install -r requirements.txt

Quick start
-----------
- Please take a look for demo project in ./demo path.
- Start your web application:

::

$ python webagent.py [--settings=<settings file>]
