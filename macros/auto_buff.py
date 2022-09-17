from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType


class AutoBuff(Macro):
    def __init__(self, key: keyboard.Key, buff_code: int, delay: int = 500):
        self.buff_code = buff_code
        self.memory_reader = MemoryReader()
        self.buff_key = key
        super().__init__(trigger_type=TriggerType.ALWAYS_TRIGGERED,
                         delay=delay)

    def action(self):
        macro_methods.click_key(self.buff_key)

    def action_condition_checker(self):
        has_buff = self.memory_reader.has_buff(self.buff_code)
        return not has_buff

