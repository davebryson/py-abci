from .messages import *
import abci.types_pb2 as types


class Result(object):
    def __init__(self, code=types.OK, data=b'', log=''):
        self.code = code
        self.data = self.__as_bytes(data)
        self.log = log

    def __as_bytes(self, d):
        if isinstance(d, str):
            return d.encode('utf-8')
        return d

    def ok(data=b'', log=''):
        data = self.__as_bytes(data)
        return Result(types.OK, data, log)

    def error(code='', data=b'',log=''):
        data = self.__as_bytes(data)
        return Result(code, data, log)

    def is_ok(self):
        return self.code == types.OK

    def str(self):
        return "ABCI[code:{}, data:{}, log:{}]".format(self.code, self.data, self.log)


class BaseApplication(object):

    def info(self):
        return to_response_info()

    def set_option(self, k, v):
        return ''

    def deliver_tx(self, tx):
        return Result.ok()

    def check_tx(self, tx):
        return Result.ok()

    def query(self, reqQuery):
        return to_response_query()

    def commit(self):
        return Result.ok()

    def begin_block(self, hash, header):
        return

    def end_block(self, height):
        # return ToResponseEndBlock
        return

    def init_chain(self, validators):
        # return ToResponseInitChain
        return
