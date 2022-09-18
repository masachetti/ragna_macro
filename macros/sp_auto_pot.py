from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType


class SpAutoPot(Macro):
    def __init__(self, key: keyboard.Key, delay: int = 500, percent_sp: int = 80):
        self.percent_sp = percent_sp
        self.memory_reader = MemoryReader()
        self.pot_key = key
        super().__init__(trigger_type=TriggerType.ALWAYS_TRIGGERED,
                         delay=delay)

    def action(self):
        macro_methods.press_key(self.pot_key)

    def action_condition_checker(self):
        max_sp = self.memory_reader.get_max_sp()
        current_sp = self.memory_reader.get_current_sp()
        current_sp_percent = (current_sp / max_sp) * 100
        return current_sp_percent <= self.percent_sp

