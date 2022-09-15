import time

from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType


class RainstormFarming(Macro):
    def __init__(self, skill_key: keyboard.Key, fly_wing_key: keyboard.Key, hotkey: keyboard.Key, map_name: str = None,
                 delay: int = 300):
        self.memory_reader = MemoryReader()
        self.skill_key = skill_key
        self.fly_wing_key = fly_wing_key
        self.map_name = map_name
        super().__init__(hotkey=hotkey,
                         trigger_type=TriggerType.TOGGLE,
                         delay=delay)

    def action(self):
        macro_methods.click_key(self.skill_key)
        time.sleep(0.05)
        macro_methods.click_mouse_lbutton()
        time.sleep(0.2)
        macro_methods.click_key(self.fly_wing_key)

    def action_condition_checker(self):
        if self.map_name:
            current_map_name = self.memory_reader.get_current_map_name()
            return self.map_name == current_map_name
        return False
