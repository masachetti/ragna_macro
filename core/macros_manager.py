from threading import Lock
from typing import List, Dict

from core.macros_monitor import MacrosMonitor
from models.macro import Macro


def setup_macros(macros):
    if isinstance(macros, dict):
        pass
    elif isinstance(macros, list):
        for macro in macros:
            macro.setup()


class MacrosManager:
    _instance = None
    _lock: Lock = Lock()
    _pause: bool = False
    _current_profile_name: str = ''
    _current_macros: List[Macro] = []
    _state_before_pause: List[bool] = []

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MacrosManager, cls).__new__(cls)
        return cls._instance

    def set_profile(self, profile_name, profile_macros):
        self._current_profile_name = profile_name
        self._current_macros = profile_macros
        self._state_before_pause = [False]*len(profile_macros)
        setup_macros(profile_macros)
        MacrosMonitor().set_macros(profile_macros)

    def pause_macros(self):
        for i, macro in enumerate(self._current_macros):
            self._state_before_pause[i] = macro.running
            macro.block()
            macro.stop()
        self._pause = True

    def release_macros(self):
        for macro, before_pause_state in zip(self._current_macros, self._state_before_pause):
            macro.unblock()
            if before_pause_state:
                macro.run()
        self._pause = False

    def toggle_macros(self):
        if self._pause:
            return self.release_macros()
        self.pause_macros()
