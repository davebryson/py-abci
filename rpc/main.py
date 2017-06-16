import json
import requests
import itertools
import binascii

from eth_utils import (
    force_bytes,
    force_obj_to_text,
    force_text,
    is_string,
    is_dict,
    decode_hex,
)

class Tendermint(object):
    def __init__(self, host="127.0.0.1", port=46657):
        self.uri = "http://{}:{}".format(host, port)
        self.session = requests.Session()
        self.request_counter = itertools.count()
        self.headers = {
            'user-agent': 'tendermint.py/0.0.1',
            'Content-Type': 'text/json'
        }

    def encode_rpc_request(self, method, params):
        return force_bytes(json.dumps(force_obj_to_text({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": str(next(self.request_counter)),
        })))

    def make_request(self, method, params):
        request_data = self.encode_rpc_request(method, params)
        response = self.session.post(
            self.uri,
            data=request_data,
            headers=self.headers,
            timeout=10
        )
        response.raise_for_status()
        return response.content

    def call(self, method, params):
        response_raw = self.make_request(method, params)
        if is_string(response_raw):
            response = json.loads(force_text(response_raw))
        elif is_dict(response_raw):
            response = response_raw

        if response["error"]:
            raise ValueError(response["error"])

        return response['result']

    def isConnected(self):
        try:
            response_raw = self.make_request('status', [])
            response = json.loads(force_text(response_raw))
        except IOError:
            return False
        else:
            assert response['jsonrpc'] == '2.0'
            assert not response['error']
            return True
        assert False

    def status(self):
        return self.call('status', [])

    def info(self):
        return self.call('abci_info', [])

    def genesis(self):
        return self.call('genesis', [])

    def net_info(self):
        return self.call('net_info', [])

    def unconfirmed_txs(self):
        return self.call('unconfirmed_txs', [])

    def validators(self):
        return self.call('validators', [])

    def get_block(self, height='latest'):
        if height == 'latest' or not height:
            v = t.status()['latest_block_height']
            return self.call('block', [v])
        if height <= 0:
            raise ValueError("Height must be greater then 0")
        return self.call('block', [height])

    def get_block_range(self, min=0, max=0):
        """ By default returns 20 blocks """
        return self.call('blockchain', [min, max])

    def get_commit(self, height=1):
        """ Get commit information for a given height """
        if height == 'latest' or not height:
            v = t.status()['latest_block_height']
            return self.call('commit', [v])
        if height <= 0:
            raise ValueError("Height must be greater then 0")
        return self.call('commit', [height])

    def query(self, path, data, proof=False):
        return self.call('abci_query', [path, data, proof])

    def send_tx_commit(self, tx):
        return self.call('broadcast_tx_commit', [tx])

    def send_tx_sync(self, tx):
        return self.call('broadcast_tx_sync', [tx])

    def send_tx_async(self, tx):
        return self.call('broadcast_tx_async', [tx])

    def get_tx(self, h, proof=False):
        """ BROKEN """
        #return self.call('tx', [h,proof])
        raise NotImplementedError("Not functional due to issue with Tendermint formatting of hash")


if __name__ == '__main__':
    """ Simple testing.  Make sure you have the counter application running """
    t = Tendermint()
    assert(t.isConnected())
    assert(t.status()["node_info"])
    assert(t.info()["response"])
    assert(t.genesis()['genesis'])
    assert(t.net_info()["listening"])
    assert(t.unconfirmed_txs()['n_txs'] >= 0)
    assert(t.validators()['block_height'] >= 0)
    assert(t.get_block()['block_meta'])
    assert(t.get_block_range()['last_height'])
    assert(t.query('','')['response'])
    assert(t.get_commit('latest')['header'])

    # Test tx: 3E5628380388EBBA0DF9F5F7A198AE2812CF5729
    #print(t.query('',''))
    #print(t.send_tx_commit('0x01'))

    # THIS DOES NOT WORK - TENDERMINT ISSUE...
    #print(t.get_tx('0xF258BE7AA640D4DB6EDA0320B6D18B1E62356E1'))
    #print(t.get_block(4303))
