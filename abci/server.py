"""
ABCI TCP server
Tendermint connects to this server over 3 different connections:
 - mempool: used for check_tx
 - consensus: used for the begin_block -> deliver_tx -> end_block -> commit flow
 - query: used to query application state

This can be a bit confusing in the app since gevent spawns a greenlet for each
connection.  If one crashes you will not have full connectivity to Tendermint
"""
import sys

import gevent, signal
from gevent.event import Event
from gevent.server import StreamServer

from .wire import *
from .messages import *
from .types_pb2 import Request
from .utils import get_logger
from .application import BaseApplication

log = get_logger()

class ProtocolHandler(object):
    """ Internal handler called by the server to process requests from
    Tendermint.  The handler delegates call to your application"""
    def __init__(self, app):
        self.app = app

    def process(self,req_type, req):
        handler = getattr(self, req_type, self.no_match)
        return handler(req)

    def echo(self, req):
        return write_message(to_response_echo(req.echo.message))

    def flush(self, req):
        flush_resp = to_response_flush()
        return write_message(to_response_flush())

    def info(self, req):
        result = self.app.info()
        response = to_response_info(result)
        return write_message(response)

    def set_option(self, req):
        result = self.app.set_option(req.set_option.key,req.set_option.value)
        response = to_response_set_option(result)
        return write_message(response)

    def check_tx(self, req):
        result = self.app.check_tx(req.check_tx.tx)
        response = to_response_check_tx(result.code, result.data, result.log)
        return write_message(response)

    def deliver_tx(self, req):
        result = self.app.deliver_tx(req.deliver_tx.tx)
        response = to_response_deliver_tx(result.code, result.data, result.log)
        return write_message(response)

    def query(self, req):
        result = self.app.query(req.query)
        response = to_response_query(result)
        return write_message(response)

    def commit(self, req):
        result = self.app.commit()
        response = to_response_commit(result.code, result.data, result.log)
        return write_message(response)

    def begin_block(self, req):
        #self.app.begin_block(req.begin_block.hash, req.begin_block.header)
        self.app.begin_block(req.begin_block)
        return write_message(to_response_begin_block())

    def end_block(self, req):
        result = self.app.end_block(req.end_block.height)
        return write_message(to_response_end_block(result))

    def init_chain(self, validators):
        log.debug("running init_chain")
        self.app.init_chain(validators)
        return write_message(to_response_init_chain())

    def no_match(self, req):
        response = to_response_exception("Unknown request!")
        return write_message(response)

class ABCIServer(object):
    def __init__(self, port=46658, app=None):
        if not app or not isinstance(app, BaseApplication):
            log.error("Application missing or not an instance of Base Application")
            raise TypeError("Application missing or not an instance of Base Application")

        self.port = port
        self.protocol = ProtocolHandler(app)
        self.server = StreamServer(('0.0.0.0', port), handle=self.__handle_connection)

    def start(self):
        self.server.start()
        log.info(" ABCIServer started on port: {}".format(self.port))

    def stop(self):
        log.info("Shutting down server")
        self.server.stop()

    def run(self):
        """Option to calling manually calling start()/stop(). This will start
        the server and watch for signals to stop the server"""
        self.server.start()
        log.info(" ABCIServer started on port: {}".format(self.port))
        # wait for interrupt
        evt = Event()
        gevent.signal(signal.SIGQUIT, evt.set)
        gevent.signal(signal.SIGTERM, evt.set)
        gevent.signal(signal.SIGINT, evt.set)
        evt.wait()
        log.info("Shutting down server")
        self.server.stop()

    # TM will spawn off 3 connections: mempool, consensus, query
    # If an error happens in 1 it still leaves the others open which
    # means you don't have all the connections available to TM
    def __handle_connection(self, socket, address):
        log.debug(' ... connection from tendermint: {}:{} ...'.format(address[0], address[1]))

        data = BytesIO()
        carry_forward = b''

        while True:
            inbound = socket.recv(1024)
            msg_length = len(carry_forward) + len(inbound)
            data.write(carry_forward)
            data.write(inbound)

            data.seek(0)
            carry_forward = b''
            if not data or msg_length == 0: return

            try:
                while data.tell() < msg_length:
                    req, err  = read_message(data, Request)
                    # TODO: an err should be 1 ...
                    # this is actually confusing see read_message
                    if err == 0: return
                    if err == -1:
                        data.seek(req)
                        carry_forward = data.read(1024)
                        break

                    req_type = req.WhichOneof("value")

                    response = self.protocol.process(req_type, req)
                    socket.sendall(response)
            except:
                log.error(" Server Error: {}".format(sys.exc_info()[1]))

            data.seek(0)
            data.truncate()
        socket.close()
