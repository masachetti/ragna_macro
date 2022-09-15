import time
from threading import Thread
from models.macro import Macro, TriggerType
from core.hotkey_listener import HotkeyListener


class MacroWrapper:
    def __init__(self, macro: Macro, name: str = None):
        self.macro = macro
        self.name = f"{macro.__class__.__name__} ({macro.hotkey})" if name is None else name
        self.delay_ms = self.macro.delay / 1000
        self.running = False
        self.hotkey_pressed = False

    def check_if_hotkey_is_being_hold(self, pressed_keys):
        if self.macro.hotkey in pressed_keys and not self.running:
            self.run()
        if self.macro.hotkey not in pressed_keys and self.running:
            self.stop()

    def check_if_hotkey_are_toggled(self, pressed_keys):
        if not self.hotkey_pressed and self.macro.hotkey in pressed_keys:
            if self.running:
                self.stop()
            else:
                self.run()
        self.hotkey_pressed = self.macro.hotkey in pressed_keys

    def run(self):
        self.running = True

        def thread_action():
            while self.running:
                if self.macro.action_condition_checker():
                    self.macro.action()
                    time.sleep(self.delay_ms)

        thread = Thread(target=thread_action, name=self.name)
        thread.start()

    def stop(self):
        self.running = False

    def setup(self):
        hotkey_listener = HotkeyListener()
        if self.macro.trigger_type == TriggerType.HOLD:
            hotkey_listener.attach_observer(self.check_if_hotkey_is_being_hold)
        if self.macro.trigger_type == TriggerType.TOGGLE:
            hotkey_listener.attach_observer(self.check_if_hotkey_are_toggled)
        if self.macro.trigger_type == TriggerType.ALWAYS_TRIGGERED:
            self.run()
