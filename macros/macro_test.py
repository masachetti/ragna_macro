import time
from pynput import keyboard
from macro import Macro, TriggerType


class MacroTest(Macro):
    def __init__(self, key: keyboard.Key, value, delay: int = 100):
        self.value = value
        super().__init__(hotkey=key,
                         trigger_type=TriggerType.ALWAYS_TRIGGERED,
                         delay=delay)

    def action(self):
        print(f"Test macro - Action - Value {self.value}")

