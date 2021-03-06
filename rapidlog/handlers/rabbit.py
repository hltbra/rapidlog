#! coding:utf-8
'''

Special handlers writes to RabbitQueue

@author: rmuslimov
@date: 24.06.2012

'''

import logging
import json
import socket

from datetime import datetime
from pika.adapters import BlockingConnection
from pika.connection import ConnectionParameters


class RabbitConnectionException(Exception):
    pass


class RabbitHandler(logging.Handler):
    '''
    host - host of RabbitMq server instance
    queue - queue name for logging
    '''

    def __init__(self, *args, **kwargs):
        self.host = kwargs.pop('host') or 'localhost'
        self.queue = kwargs.pop('queue') or 'logging'
        self.quiet = kwargs.pop('quiet', False)

        # old style class __init__
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        msg = self.format(record)

        body = json.dumps({
            'msg': msg,
            'loggername': record.name,
            'level': record.levelname,
            'created': datetime.now().isoformat()
        })

        try:
            con = BlockingConnection(ConnectionParameters(self.host))
        except socket.error:
            raise RabbitConnectionException('Connection to {0} failed'.format(\
                self.host))
        channel = con.channel()

        channel.queue_declare(queue=self.queue, durable=True,
                              exclusive=False, auto_delete=False)

        channel.basic_publish(exchange='',\
                              routing_key=self.queue,\
                              body=body)
        con.close()
