import time
from core import macro_methods
from pynput import keyboard
from models.macro import Macro, TriggerType


class ClickSpam(Macro):
    def __init__(self, key: keyboard.Key, delay: int = 100):
        super().__init__(hotkey=key,
                         trigger_type=TriggerType.HOLD,
                         delay=delay)

    def action(self):
        macro_methods.lbutton_mouse_click()
        macro_methods.delay(20)
