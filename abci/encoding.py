
from io import BytesIO

# Codes
NODATA = 1
FRAGDATA = 2
OK = 3

def _byte(b):
    return bytes((b, ))

def encode(number):
    # Shift to int64
    number = number << 1
    buf = b''
    while True:
        towrite = number & 0x7f
        number >>= 7
        if number:
            buf += _byte(towrite | 0x80)
        else:
            buf += _byte(towrite)
            break
    return buf

def decode_stream(stream):
    shift = 0
    result = 0
    while True:
        i = _read_one(stream)
        result |= (i & 0x7f) << shift
        shift += 7
        if not (i & 0x80):
            break

    return result

def _read_one(stream):
    c = stream.read(1)
    if c == b'':
        raise EOFError("Unexpected EOF while reading bytes")
    return ord(c)

def write_message(message):
    buffer = BytesIO(b'')
    bz = message.SerializeToString()
    #buffer.write(_VarintBytes(len(bz)))
    buffer.write(encode(len(bz)))
    buffer.write(bz)
    return buffer.getvalue()

def read_varint(reader):
    len64 = decode_stream(reader)
    length = len64 >> 1
    return length, reader.read(length)

def read_message(reader, message):
    """ read the message based on the varintself.
    Returns: (value, code) based on results
    """
    current_position = reader.tell()
    length, slice = read_varint(reader)

    if len(slice) == 0:
        return None, NODATA

    if len(slice) < length:
        return current_position, FRAGDATA

    m = message()
    m.ParseFromString(slice)
    return m, OK
