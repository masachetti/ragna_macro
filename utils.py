

def parse_bytes_to_uint32(byte_values):
    return int.from_bytes(byte_values, byteorder='little', signed=False)


def parse_bytes_to_string(byte_values):
    return ''.join(map(chr, byte_values))


def parse_hex_string_to_int(hex_string):
    try:
        return int(hex_string, 16)
    except Exception as e:
        return None
