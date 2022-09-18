import importlib
import json
import os
import sys


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


def load_servers_info():
    content = None
    with open('resources/servers_info.json') as json_file:
        content = json.load(json_file)
    return content
