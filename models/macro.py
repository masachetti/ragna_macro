from dataclasses import dataclass
import enum
from pynput import keyboard


class TriggerType(enum.Enum):
    HOLD = enum.auto()
    TOGGLE = enum.auto()
    ALWAYS_TRIGGERED = enum.auto()


@dataclass
class Macro:
    hotkey: keyboard.Key = None
    trigger_type: TriggerType = None
    delay: int = 500

    def action(self):
        return

    def action_condition_checker(self):
        return True
