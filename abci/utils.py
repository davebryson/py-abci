# Common functions needed
import binascii
from math import ceil

def str_to_bytes(data):
    if isinstance(data, str):
        return data.encode('utf-8')
    return data

def bytes_to_str(value):
    if isinstance(value, str):
        return value
    return value.decode('utf-8')

def int_to_big_endian(value):
    byte_length = max(ceil(value.bit_length() / 8), 1)
    return (value).to_bytes(byte_length, byteorder='big')

def big_endian_to_int(value):
    return int.from_bytes(value, byteorder='big')

def decode_hex(s):
    if isinstance(s, str):
        return bytes.fromhex(s)
    if isinstance(s, (bytes, bytearray)):
        return binascii.unhexlify(s)
    raise TypeError('Value must be an instance of str or bytes')

def encode_hex(b):
    if isinstance(b, str):
        b = bytes(b, 'utf-8')
    if isinstance(b, (bytes, bytearray)):
        return str(binascii.hexlify(b), 'utf-8')
    raise TypeError('Value must be an instance of str or bytes')
