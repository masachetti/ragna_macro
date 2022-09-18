import importlib
import importlib.util
import os
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from pick import pick

from core.hotkey_listener import HotkeyListener
from core.macros_monitor import MacrosMonitor
from models.macro import Macro
from utils import loaders

@dataclass
class App:
    servers_info: Dict = field(init=False)
    profiles: Dict[str, List[Macro]] = field(init=False)
    enabled_profile: Tuple[str, List[Macro]] = field(init=False)
    # def __init__(self):
        # self.enabled_profile = list(self.profiles.items())[0] if self.profiles else None

    def run_client_picker(self):
        pass

    def run_profile_picker(self):
        title = "Choose the profile: "
        options = list(self.profiles.keys())
        option, index = pick(options, title)
        self.set_profile(option)

    def set_profile(self, profile_name):
        if profile_name in self.profiles:
            self.enabled_profile = (profile_name, self.profiles[profile_name])

    def start(self):
        print("Starting App")
        print("- Loading servers info")
        self.servers_info = loaders.load_servers_info()
        print("- Loading profiles")
        self.profiles = loaders.load_profiles()
        print("- Search for Rag clients")

        print("Client Pick")
        print("- Setup client window handler")
        print("- Setup client process handler")
        print("Profile pick")
        print("- Importing profile")
        print("- Setup macros")
        print("- Start macros")
        print("Macro monitor view")

        self.run_profile_picker()
        hotkey_listener = HotkeyListener()
        hotkey_listener.start()
        if self.enabled_profile:
            print(f"Enabled profile: {self.enabled_profile[0]}")
            macros = self.enabled_profile[1]
            if isinstance(macros, dict):
                pass
            elif isinstance(macros, list):
                for macro in macros:
                    macro.setup()
                    print(f"- {macro.name}")

            macro_monitor = MacrosMonitor(macros)
            macro_monitor.start()
        # hotkey_listener.listener.join()


if __name__ == '__main__':
    app = App()
    app.start()