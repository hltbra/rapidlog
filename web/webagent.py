#! coding:utf-8
'''
Simple tornado app for handling messages from RabbitMq

@author: rmuslimov
@date: 26.06.2012

'''
import os
from uuid import uuid1

import pika
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
from pika.adapters.tornado_connection import TornadoConnection
from tornado.options import options, define, parse_config_file,\
     parse_command_line


define("settings", default=None, help="settings file")

define("port", default=8000, type=int, help="run on the given port")
define("queue_name", default="logging", help="Logging queue name")
define("queue_host", default="127.0.0.1", help="Host for amqp daemon")
define("queue_port", default=5672, help="amqp server port")
define("queue_user", default="guest", help="User for amqp daemon")
define("queue_pasw", default="guest", help="Password for amqp daemon")
define("loggers", default=[], help="Loggers to watch")

parse_command_line()

# Unique keys generator
genid = lambda _: str(uuid1())[:7]


class WebSocketsManager(object):
    '''
    Managing sockets and send messages
    '''
    sockets = {}

    def add_socket(self, socket):
        key = genid()
        self.sockets[key] = socket
        return key

    def close_socket(self, key):
        del self.sockets[key]

    def process_message(self, message):
        for each in self.sockets.itervalues():
            each.write_message(message)


class RabbitClient(object):
    '''
    Managing incoming messages from Rabbit Service
    '''

    def __init__(self, app=None):
        self.app = app
        credentials = pika.PlainCredentials(options.queue_user,\
                                            options.queue_pasw)
        param = pika.ConnectionParameters(host=options.queue_host,
                                          port=options.queue_port,
                                          virtual_host="/",
                                          credentials=credentials)
        TornadoConnection(param, on_open_callback=self.on_connected)

    def on_connected(self, con):
        con.channel(self.on_channel_open)

    def on_channel_open(self, channel):
        channel.basic_consume(consumer_callback=self.on_message,
                              queue=options.queue_name,
                              no_ack=True)

    def on_message(self, channel, method, header, body):
        self.app.wmanager.process_message(body)


class WebSocket(tornado.websocket.WebSocketHandler):
    '''
    Websocket instance
    '''
    idx = None

    def open(self):
        app = self.application
        self.idx = app.wmanager.add_socket(self)

    def on_close(self):
        app = self.application
        app.wmanager.close_socket(self.idx)


class IndexView(tornado.web.RequestHandler):
    '''
    Rendering index page
    '''
    def get(self):
        self.render("index.html", loggers=options.loggers)


class TornadoWebServer(tornado.web.Application):
    '''
    Serve websockets and main web page
    '''

    # Rabbit connection manager
    rmanager = None
    # Websockets amanger
    wmanager = None

    def __init__(self):
        handlers = (
            (r"/", IndexView),
            (r"/ws", WebSocket),
            )

        relative = lambda x: os.path.join(os.path.dirname(__file__), x)
        settings = dict(
            template_path=relative('templates'),
            static_path=relative("static"),
            debug=True
        )

        tornado.web.Application.__init__(self, handlers, **settings)

    def initManagers(self):
        self.rmanager = RabbitClient(self)
        self.wmanager = WebSocketsManager()


if __name__ == '__main__':
    # Set our pika.log options
    pika.log.setup(color=True)

    #Tornado Application
    pika.log.info("Initializing RapidLogs Tornado...")

    app = TornadoWebServer()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    # Get a handle to the instance of IOLoop
    ioloop = tornado.ioloop.IOLoop.instance()

    # Add our Pika connect to the IOLoop since we loop on ioloop.start
    ioloop.add_timeout(100, app.initManagers)

    # Start the IOLoop
    ioloop.start()
