from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType


class AutoBuffWithMultipleKeys(Macro):
    def __init__(self, keys: [keyboard.Key | str], buff_code: int, delay: int = 500):
        self.buff_code = buff_code
        self.memory_reader = MemoryReader()
        self.buff_key = keys
        super().__init__(trigger_type=TriggerType.ALWAYS_TRIGGERED,
                         delay=delay)

    def action(self):
        for key in self.buff_key:
            macro_methods.press_key(key)
            macro_methods.delay(500)

    def action_condition_checker(self):
        has_buff = self.memory_reader.has_buff(self.buff_code)
        return not has_buff

