import time
from core import macro_methods
from pynput import keyboard
from models.macro import Macro, TriggerType


class PRMManualSwap(Macro):
    def __init__(self, key: keyboard.Key, manual_key: keyboard.Key, skill_key: keyboard.Key, default_manual_key:keyboard.Key):
        self.manual_key=manual_key
        self.skill_key=skill_key
        self.default_manual_key=default_manual_key
        super().__init__(hotkey=key,
                         trigger_type=TriggerType.HOLD,
                         delay=500)

    def action(self):
        macro_methods.press_key(self.manual_key)
        time.sleep(0.2)
        macro_methods.press_key(self.skill_key)
        time.sleep(1.5)
        macro_methods.press_key(self.default_manual_key)

