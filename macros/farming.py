import time

from core import macro_methods
from pynput import keyboard

from core.memory_reader import MemoryReader
from models.macro import Macro, TriggerType

NUMBER_OF_ACTIONS_TO_GET_ARROWS = 47


class RainstormFarming(Macro):
    def __init__(self, skill_key: keyboard.Key, fly_wing_key: keyboard.Key, hotkey: keyboard.Key, map_name: str = None,
                 arrow_pack_key: keyboard.Key = None, delay: int = 300):
        self.memory_reader = MemoryReader()
        self.skill_key = skill_key
        self.fly_wing_key = fly_wing_key
        self.map_name = map_name
        self.arrow_pack_key = arrow_pack_key
        self._action_counter = 0
        super().__init__(hotkey=hotkey,
                         trigger_type=TriggerType.TOGGLE,
                         delay=delay)

    def action(self):
        self.count_and_open_arrow_pack()
        macro_methods.press_key(self.skill_key)
        time.sleep(0.05)
        macro_methods.lbutton_mouse_click()
        time.sleep(0.2)
        macro_methods.press_key(self.fly_wing_key)

    def count_and_open_arrow_pack(self):
        if self.arrow_pack_key:
            self._action_counter += 1
            if self._action_counter >= NUMBER_OF_ACTIONS_TO_GET_ARROWS:
                macro_methods.press_key(self.arrow_pack_key)
                self._action_counter = 0

    def action_condition_checker(self):
        if self.map_name:
            current_map_name = self.memory_reader.get_current_map_name()
            return self.map_name == current_map_name
        return False
