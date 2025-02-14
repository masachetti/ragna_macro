import time
from core import macro_methods
from pynput import keyboard
from models.macro import Macro, TriggerType


class SkillRotation(Macro):
    def __init__(self, key: keyboard.Key, skill_keys: [keyboard.Key], delay: int = 500):
        self.skill_keys = skill_keys
        self.i = 0
        super().__init__(hotkey=key,
                         trigger_type=TriggerType.HOLD,
                         delay=delay)

    def action(self):
        macro_methods.press_key(self.skill_keys[self.i])
        time.sleep(0.05)
        macro_methods.lbutton_mouse_click()
        self.i = (self.i + 1) % len(self.skill_keys)
