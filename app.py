from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from pick import pick

from core.client_handler import ClientHandler
from core.hotkey_listener import HotkeyListener
from core.macros_monitor import MacrosMonitor
from models.macro import Macro
from utils import loaders, win32_utils
from utils.wrapped_pick import WrappedPicker


@dataclass
class App:
    servers_info: Dict = field(init=False)
    profiles: Dict[str, List[Macro]] = field(init=False)
    enabled_profile: Tuple[str, List[Macro]] = field(init=False)

    def start(self):
        self.load_servers_info()
        self.load_profiles()

        self.run_client_picker()
        self.run_profile_picker()

        hotkey_listener = HotkeyListener()
        hotkey_listener.start()
        if self.enabled_profile:
            macros = self.enabled_profile[1]
            if isinstance(macros, dict):
                pass
            elif isinstance(macros, list):
                for macro in macros:
                    macro.setup()

            macro_monitor = MacrosMonitor(macros)
            macro_monitor.start()
        # hotkey_listener.listener.join()

    def load_servers_info(self):
        self.servers_info = loaders.load_servers_info()

    def load_profiles(self):
        self.profiles = loaders.load_profiles()

    def set_profile(self, profile_name):
        if profile_name in self.profiles:
            self.enabled_profile = (profile_name, self.profiles[profile_name])

    def run_client_picker(self):
        server_names_by_title = {server_info['window_title']: server_name for server_name, server_info in
                                 self.servers_info.items()}
        valid_windows = win32_utils.get_windows_with_valid_title(list(server_names_by_title.keys()))

        def window_focus_callback(option_info):
            _index = option_info[1]
            hwnd = valid_windows[_index][0]
            win32_utils.flash_and_bring_the_window_to_top(hwnd)

        picker_title = "Choose a client (Press F1 to flash or bring the window to top):"
        options = [f"{pid} - {server_names_by_title[title]}" for hwnd, title, pid in valid_windows]
        picker = WrappedPicker(window_focus_callback, options=options, title=picker_title, indicator="->")
        option, index = picker.start()
        selected_hwnd = valid_windows[index][0]
        ClientHandler().set_window_handler(selected_hwnd)

    def run_profile_picker(self):
        title = "Choose profile: "
        options = list(self.profiles.keys())
        option, index = pick(options, title, indicator="->")
        self.set_profile(option)


if __name__ == '__main__':
    app = App()
    app.start()
