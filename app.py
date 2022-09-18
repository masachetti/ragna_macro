import importlib
import importlib.util
import os
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import win32gui
import win32process
from pick import pick

from core.hotkey_listener import HotkeyListener
from core.macros_monitor import MacrosMonitor
from models.macro import Macro
from utils import loaders, win32_utils


@dataclass
class App:
    servers_info: Dict = field(init=False)
    profiles: Dict[str, List[Macro]] = field(init=False)
    enabled_profile: Tuple[str, List[Macro]] = field(init=False)

    # def __init__(self):
    # self.enabled_profile = list(self.profiles.items())[0] if self.profiles else None

    def load_servers_info(self):
        self.servers_info = loaders.load_servers_info()

    def load_profiles(self):
        self.profiles = loaders.load_profiles()

    def run_client_picker(self):
        server_names_by_title = {server_info['window_title']: server_name for server_name, server_info in
                                 self.servers_info.items()}
        valid_windows = win32_utils.get_windows_with_valid_title(list(server_names_by_title.keys()))

        picker_title = "Choose a client: "
        options = [f"{pid} - {server_names_by_title[title]}" for hwnd, title, pid in valid_windows]
        option, index = pick(options, picker_title)
        print(option)

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
        self.load_servers_info()
        print("- Loading profiles")
        self.load_profiles()
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
