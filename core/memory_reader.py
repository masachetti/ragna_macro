import json
from threading import Lock

import utils
from core.client_handler import ClientHandler
uint = utils.parse_bytes_to_uint32

class MemoryReader(object):
    _instance = None
    _lock: Lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MemoryReader, cls).__new__(cls)
                cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.addresses = parse_addresses(load_addresses())
        self.client = ClientHandler()
        self.get_current_hp = self._create_reader_function('current-hp', 4, uint)
        self.get_current_map_name = self._create_reader_function('current-map-name', 25, extract_map_name)

    def _create_reader_function(self, address_name, memory_len, value_parser):
        def reader():
            if address_name in self.addresses:
                address = self.addresses[address_name]
            else:
                raise ValueError(f"Can't find '{address_name}' in the addresses list, check the file addresses.json.")
            if address:
                memory_value = self.client.read_address(address, memory_len)
                parsed_value = value_parser(memory_value)
                return parsed_value
            else:
                raise SyntaxError(f"Incorrect address for '{address_name}', check the file addresses.json.")
        return reader


def extract_map_name(map_name_bytes):
    return utils.parse_bytes_to_string(map_name_bytes.split(b'\00')[0])

    
def parse_addresses(addresses):
    return dict(map(lambda x: (x[0], utils.parse_hex_string_to_int(x[1])), addresses.items()))


def load_addresses():
    content = None
    with open('../addresses.json') as json_file:
        content = json.load(json_file)
    return content
