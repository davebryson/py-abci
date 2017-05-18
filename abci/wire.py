#import struct
from io import BytesIO
import abci.utils as util

"""
def __structcodes(length):
    if length == 1:
        return '>B'
    if length == 2:
        return '>H'
    if length == 4:
        return '>I'
    if length == 8:
        return '>Q'
"""

def uvarint_size(i):
    if i == 0:
        return 0
    for j in [1,2,3,4,5,6,7,8]:
        if i < 1 << j * 8:
            return j
    return 8

def write_varint(i, writer):
    negate = False
    if i < 0:
        negate = True
        i = -i
    size = uvarint_size(i)
    if size == 0:
        return writer.write(0)
    big_end = util.int_to_big_endian(i)
    if negate:
        size += 0xF0
    writer.write(bytes([size]))
    writer.write(big_end)

def read_varint(reader):
    b = reader.read(1)
    if len(b) == 0:
        return 0
    size = util.big_endian_to_int(b)
    negate = False
    if size >> 4 == 0xF:
        negate = True
        size = size & 0x0F
    if size == 0 or size > 8:
        return 0
    rest = reader.read(size)
    if len(rest) < size:
        return 0
    i = util.big_endian_to_int(rest)
    if negate:
        return -i
    else:
	    return i

def write_byte_slice(bz, buffer):
    write_varint(len(bz), buffer)
    buffer.write(bz)

def read_byte_slize(reader):
    length = read_varint(reader)
    return reader.read(length)

def write_message(message):
    buffer = BytesIO(b'')
    bz = message.SerializeToString()
    write_byte_slice(bz, buffer)
    return buffer.getvalue()

def read_message(reader, message):
    bsliced = read_byte_slize(reader)
    if len(bsliced) == 0:
        return None, 0
    m = message()
    m.ParseFromString(bsliced)
    return m, 1
