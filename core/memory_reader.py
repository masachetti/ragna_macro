import json
from threading import Lock

from utils import utils
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
        self.get_max_hp = self._create_reader_function('max-hp', 4, uint)
        self.get_current_sp = self._create_reader_function('current-sp', 4, uint)
        self.get_max_sp = self._create_reader_function('max-sp', 4, uint)
        self.get_current_weight = self._create_reader_function('weight', 4, uint)
        self.get_max_weight = self._create_reader_function('max-weight', 4, uint)
        self.get_current_map_name = self._create_reader_function('current-map-name', 25, extract_map_name)
        self.get_coordinate_x = self._create_reader_function('coordinate-x', 4, uint)
        self.get_coordinate_y = self._create_reader_function('coordinate-y', 4, uint)
        self.get_buffs = self._create_reader_function('coordinate-y', 4 * 100, extract_buffs)

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


def extract_buffs(buffs_bytes):
    return None


def extract_map_name(map_name_bytes):
    return utils.parse_bytes_to_string(map_name_bytes.split(b'\00')[0])


def parse_addresses(addresses):
    return dict(map(lambda x: (x[0], utils.parse_hex_string_to_int(x[1])), addresses.items()))


def load_addresses():
    content = None
    with open('resources/addresses.json') as json_file:
        content = json.load(json_file)
    return content


if __name__ == '__main__':
   mem = MemoryReader()
   print(f"Current Hp: {mem.get_current_hp()}")
   print(f"Max Hp: {mem.get_max_hp()}")
   print(f"Current Sp: {mem.get_current_sp()}")
   print(f"Max Sp: {mem.get_max_sp()}")
   print(f"Current W: {mem.get_current_weight()}")
   print(f"Max W: {mem.get_max_weight()}")
   print(f"Current Map: {mem.get_current_map_name()}")
   print(f"X: {mem.get_coordinate_x()}")
   print(f"Y: {mem.get_coordinate_y()}")