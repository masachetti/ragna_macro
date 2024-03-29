import time
import enum
from dataclasses import dataclass, field
from threading import Thread
from typing import Callable

from pynput import keyboard
from core.hotkey_listener import HotkeyListener

MIN_THREAD_DELAY = 0.01


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
    action_condition: bool = field(init=False, default=True)
    _ms_delay: float = field(init=False)
    _hotkey_pressed: bool = field(init=False, default=False)
    _blocked: bool = field(init=False, default=False)
    _listener_callback: Callable = field(init=False, default=None)

    def __post_init__(self):
        if self.name is None:
            self.name = self.__class__.__name__
        self._ms_delay = self.delay / 1000

    def action(self):
        return

    def action_condition_checker(self):
        return True

    def run(self):
        if self._blocked:
            return

        self.running = True

        def thread_action():
            while self.running:
                self.action_condition = self.action_condition_checker()
                if self.action_condition:
                    self.action()
                    time.sleep(self._ms_delay)
                    continue
                time.sleep(MIN_THREAD_DELAY)

        thread = Thread(target=thread_action, name=self.name)
        thread.start()

    def stop(self):
        self.running = False

    def block(self):
        self._blocked = True

    def unblock(self):
        self._blocked = False

    def setup(self):
        hotkey_listener = HotkeyListener()
        if self.trigger_type == TriggerType.HOLD:
            self._listener_callback = hotkey_listener.attach_observer(self._check_if_hotkey_is_being_hold)
        if self.trigger_type == TriggerType.TOGGLE:
            self._listener_callback = hotkey_listener.attach_observer(self._check_if_hotkey_are_toggled)
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

    def __delete__(self, instance):
        if instance._listener_callback:
            HotkeyListener().detach_observer(instance._listener_callback)
