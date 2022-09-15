import importlib
import importlib.util
import os
import sys

from core.hotkey_listener import HotkeyListener
from models.macro_wrapper import MacroWrapper


class App:
    def __init__(self):
        self.profiles = load_profiles()
        self.enabled_profile = list(self.profiles.items())[0] if self.profiles else None

    def set_profile(self, profile_name):
        if profile_name in self.profiles:
            self.enabled_profile = (profile_name, self.profiles[profile_name])

    def start(self):
        print("Starting App")
        hotkey_listener = HotkeyListener()
        hotkey_listener.start()
        if self.enabled_profile:
            print(f"Enabled profile: {self.enabled_profile[0]}")
            macros = self.enabled_profile[1]
            if isinstance(macros, dict):
                pass
            elif isinstance(macros, list):
                for macro in macros:
                    wrapped_macro = MacroWrapper(macro)
                    wrapped_macro.setup()

        hotkey_listener.listener.join()


def load_profiles():
    profiles_path = r'profiles'
    profile_files = dict()
    profiles = dict()

    for root, directories, files in os.walk(profiles_path):
        for f in files:
            if f.endswith(".py"):
                profile_files[f] = os.path.join(root, f)

    for file_name, profile_file_path in profile_files.items():
        profile_name = file_name.split('.')[0]
        module_name = f"profiles.{profile_name}"
        spec = importlib.util.spec_from_file_location(module_name, profile_file_path)
        foo = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = foo
        spec.loader.exec_module(foo)
        profiles[profile_name] = foo.macros

    return profiles


if __name__ == '__main__':
    app = App()
    app.start()