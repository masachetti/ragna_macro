import time
from core import macro_methods
from pynput import keyboard
from models.macro import Macro, TriggerType


class SkillSpam(Macro):
    def __init__(self, key: keyboard.Key, delay: int = 100):
        super().__init__(hotkey=key,
                         trigger_type=TriggerType.HOLD,
                         delay=delay)

    def action(self):
        macro_methods.press_key(self.hotkey)
        time.sleep(0.05)
        macro_methods.lbutton_mouse_click()
