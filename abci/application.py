from messages import *
import abci.types_pb2 as types


class Result(object):
    def __init__(self, code=0, data='0', log=''):
        self.code = code
        self.data = data
        self.log = log

    def ok(data='', log=''):
        return Result(types.CodeType.OK, data, log)

    def error(code='', data='',log=''):
        return Result(code, data, log)

    def is_ok(self):
        return self.code == types.CodeType.OK

    def str(self):
        return "ABCI[code:{}, data:{}, log:{}]".format(self.code, self.data, self.log)


class BaseApplication(object):

    def info(self):
        return to_response_info()

    def set_option(self, k, v):
        pass

    def deliver_tx(self, tx):
        return Result.ok()

    def check_tx(self, tx):
        return Result.ok()

    def commit(self):
        pass
