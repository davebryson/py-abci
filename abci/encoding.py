from io import BytesIO


def encode_varint(number):
    # Shift to int64
    number = number << 1
    buf = b''
    while True:
        towrite = number & 0x7f
        number >>= 7
        if number:
            buf += bytes((towrite | 0x80,))
        else:
            buf += bytes((towrite,))
            break
    return buf

def decode_varint(stream):
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
    buffer.write(encode_varint(len(bz)))
    buffer.write(bz)
    return buffer.getvalue()


def read_messages(reader, message):
    """Return an interator of the messages found in
    the `reader` (BytesIO instance)."""

    while True:
        try:
            length = decode_varint(reader) >> 1
        except EOFError:
            return

        data = reader.read(length)

        if len(data) < length:
            return

        m = message()
        m.ParseFromString(data)

        yield m
