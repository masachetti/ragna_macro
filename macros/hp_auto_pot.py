from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType


class HpAutoPot(Macro):
    def __init__(self, key: keyboard.Key, delay: int = 500, percent_hp: int = 80):
        self.percent_hp = percent_hp
        self.memory_reader = MemoryReader()
        self.pot_key = key
        super().__init__(trigger_type=TriggerType.ALWAYS_TRIGGERED,
                         delay=delay)

    def action(self):
        macro_methods.press_key(self.pot_key)

    def action_condition_checker(self):
        max_hp = self.memory_reader.get_max_hp()
        current_hp = self.memory_reader.get_current_hp()
        current_hp_percent = (current_hp / max_hp) * 100
        return current_hp_percent <= self.percent_hp

