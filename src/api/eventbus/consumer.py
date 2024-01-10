import asyncio
import functools
import json
import logging

import pika
from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exchange_type import ExchangeType

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')
logger = logging.getLogger(__name__)


class AsyncioRabbitMQ(object):
    EXCHANGE = 'lighter'
    EXCHANGE_TYPE = ExchangeType.topic
    QUEUE = ''
    ROUTING_KEYS = [
        'server_update',
        'room_update'
    ]

    def __init__(self, amqp_url):
        self._connection = None
        self._channel = None

        self._deliveries = []
        self._acked = 0
        self._nacked = 0
        self._message_number = 0

        self._stopping = False
        self._url = amqp_url

    def connect(self):
        logger.info('Connecting to %s', self._url)
        return AsyncioConnection(
            pika.URLParameters(self._url),
            on_open_callback=self.on_connection_open,
            on_open_error_callback=self.on_connection_open_error,
            on_close_callback=self.on_connection_closed)

    def on_connection_open(self, connection):
        logger.info('Connection opened')
        self._connection = connection
        logger.info('Creating a new channel')
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_connection_open_error(self, _unused_connection, err):
        logger.error('Connection open failed: %s', err)

    def on_connection_closed(self, _unused_connection, reason):
        logger.warning('Connection closed: %s', reason)
        self._channel = None

    def on_channel_open(self, channel):
        logger.info('Channel opened')
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange(self.EXCHANGE)

    def add_on_channel_close_callback(self):
        logger.info('Adding channel close callback')
        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reason):
        logger.warning('Channel %i was closed: %s', channel, reason)
        self._channel = None
        if not self._stopping:
            self._connection.close()

    def setup_exchange(self, exchange_name):
        logger.info('Declaring exchange %s', exchange_name)
        # Note: using functools.partial is not required, it is demonstrating
        # how arbitrary data can be passed to the callback when it is called
        cb = functools.partial(self.on_exchange_declareok, userdata=exchange_name)
        self._channel.exchange_declare(exchange=exchange_name, exchange_type=self.EXCHANGE_TYPE, callback=cb)

    def on_exchange_declareok(self, _unused_frame, userdata):
        logger.info('Exchange declared: %s', userdata)
        # self.setup_queue(self.QUEUE)  # -> change to setup_routing_key
        for routing_key in self.ROUTING_KEYS:
            self.setup_queue(routing_key)

    def setup_queue(self, routing_key):
        logger.info('Declaring queue %s', routing_key)
        cb = functools.partial(self.on_queue_declareok, routing_key=routing_key)
        self._channel.queue_declare(queue=routing_key, callback=cb)

    def on_queue_declareok(self, _unused_frame, routing_key):
        logger.info('Binding %s to %s with %s', self.EXCHANGE, routing_key, routing_key)
        self._channel.queue_bind(routing_key, self.EXCHANGE, routing_key=routing_key, callback=self.on_bindok)

    def on_bindok(self, _unused_frame):
        logger.info('Queue bound')

    def read_messages(self, routing_key, callback):
        cb = functools.partial(self._on_message, upper_callback=callback)
        self._channel.basic_consume(routing_key, cb)

    def _on_message(self, _unused_channel, basic_deliver, properties, body, upper_callback):
        asyncio.create_task(upper_callback(body))
        self._channel.basic_ack(basic_deliver.delivery_tag)
