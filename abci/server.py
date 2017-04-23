import crayons
from .wire import *
from .messages import *
from .application import BaseApplication

from gevent.server import StreamServer

def info_message(txt):
    print(" >> {}".format(txt))

def ok_message(txt):
    print(" >> {}".format(crayons.green(txt)))

def err_message(txt):
    print(" >> {}".format(crayons.red(txt)))

def warn_message(txt):
    print(" >> {}".format(crayons.yellow(txt)))


class ProtocolHandler(object):

    def __init__(self, app):
        self.app = app

    def process(self,req_type, req):
        handler = getattr(self,req_type, self.no_match)
        return handler(req)

    def echo(self, req):
        return write_message(to_response_echo(req.echo.message))

    def flush(self, req):
        flush_resp = to_response_flush()
        return write_message(to_response_flush())

    def info(self, req):
        response = self.app.info()
        return write_message(response)

    def set_option(self, req):
        # TODO
        return b''

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
        #TODO
        return b''

    def begin_block(self, req):
        # TODO
        return b''
    def end_block(self, req):
        # TODO
        return b''
    def init_chain(self, validators):
        # TODO
        return b''


    def no_match(self, req):
        response = to_response_exception("Unknown request!")
        return write_message(response)


class ABCIServer(object):

    def __init__(self, port=46658, app=None):
        if not app or not isinstance(app, BaseApplication):
            raise Exception(crayons.red("Application missing or not an instance of Base Application"))
        self.port = port
        self.protocol = ProtocolHandler(app)
        self.server = StreamServer(('0.0.0.0', port), handle=self.__handle_connection)

    def start(self):
        self.server.start()
        ok_message("ABCIServer started on port: {}".format(self.port))

    def stop(self):
        self.server.stop()

    def __handle_connection(self, socket, address):
        ok_message('New connection from: {}:{}'.format(address[0], address[1]))
        while True:
            inbound = socket.recv(1024)
            msg_length = len(inbound)
            data = BytesIO(inbound)
            #info_message('len {}'.format(msg_length))
            if not data or msg_length == 0: return

            while data.tell() < msg_length:
                try:
                    req, err  = read_message(data, types.Request)
                    if err == 0: return

                    req_type = req.WhichOneof("value")
                    response = self.protocol.process(req_type, req)
                    socket.sendall(response)

                except Exception as e:
                    print(crayons.red(e))

        socket.close()
