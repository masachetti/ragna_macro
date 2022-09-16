import time
import enum
from dataclasses import dataclass, field
from threading import Thread
from pynput import keyboard
from core.hotkey_listener import HotkeyListener


class TriggerType(enum.Enum):
    HOLD = enum.auto()
    TOGGLE = enum.auto()
    ALWAYS_TRIGGERED = enum.auto()


@dataclass
class Macro:
    name: str = None
    hotkey: keyboard.Key = None
    trigger_type: TriggerType = None
    delay: int = 500
    running: bool = field(init=False, default=False)
    _ms_delay: float = field(init=False)
    _hotkey_pressed: bool = field(init=False, default=False)

    def __post_init__(self):
        if self.name is None:
            self.name = self.__class__.__name__
        self._ms_delay = self.delay / 1000

    def action(self):
        return

    def action_condition_checker(self):
        return True

    def run(self):
        self.running = True

        def thread_action():
            while self.running:
                if self.action_condition_checker():
                    self.action()
                    time.sleep(self._ms_delay)

        thread = Thread(target=thread_action, name=self.name)
        thread.start()

    def stop(self):
        self.running = False

    def setup(self):
        hotkey_listener = HotkeyListener()
        if self.trigger_type == TriggerType.HOLD:
            hotkey_listener.attach_observer(self._check_if_hotkey_is_being_hold)
        if self.trigger_type == TriggerType.TOGGLE:
            hotkey_listener.attach_observer(self._check_if_hotkey_are_toggled)
        if self.trigger_type == TriggerType.ALWAYS_TRIGGERED:
            self.run()

    def _check_if_hotkey_is_being_hold(self, pressed_keys):
        if self.hotkey in pressed_keys and not self.running:
            self.run()
        if self.hotkey not in pressed_keys and self.running:
            self.stop()

    def _check_if_hotkey_are_toggled(self, pressed_keys):
        if not self._hotkey_pressed and self.hotkey in pressed_keys:
            if self.running:
                self.stop()
            else:
                self.run()
        self._hotkey_pressed = self.hotkey in pressed_keys
