import crayons
from abci.wire import *
from abci.messages import *
from abci.application import BaseApplication

from gevent.server import StreamServer

def info_message(txt):
    print(" >> {}".format(txt))

def ok_message(txt):
    print(" >> {}".format(crayons.green(txt)))

def err_message(txt):
    print(" >> {}".format(crayons.red(txt)))

def warn_message(txt):
    print(" >> {}".format(crayons.yellow(txt)))


class ABCIServer(object):

    # Todo App
    def __init__(self, port=46658, app=None):
        if not app or not isinstance(app, BaseApplication):
            raise Exception(crayons.red("Application missing or not an instance of Base Application"))
        self.port = port
        self.app = app
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
            info_message('len {}'.format(msg_length))

            if not data or msg_length == 0: return

            while data.tell() < msg_length:
                try:
                    req, err  = read_message(data, types.Request)
                    if err == 0: return

                    self.__on_request(req, socket)

                except Exception as e:
                    print(e)
                    socket.close()

        socket.close()


    def __on_request(self, req, socket):
        req_type = req.WhichOneof("value")

        if req_type == 'echo':
            raw = write_message(to_response_echo(req.echo.message))
            socket.sendall(raw)
        if req_type == 'flush':
            flush_resp = to_response_flush()
            raw = write_message(to_response_flush())
            socket.send(raw)
        # App
        if req_type == 'info':
            response = self.app.info()
            raw = write_message(response)
            socket.send(raw)
        if req_type == 'deliver_tx':
            result = self.app.deliver_tx(req.tx)
            response = to_response_deliver_tx(result.code, result.data, result.log)
            raw = write_message(response)
            socket.send(raw)
        if req_type == 'check_tx':
            result = self.app.check_tx(req.tx)
            response = to_response_check_tx(result.code, result.data, result.log)
            raw = write_message(response)
            socket.send(raw)
