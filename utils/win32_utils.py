from typing import List

import win32gui
import win32process


def get_windows_with_valid_title(title_list: List[str]):
    valid_windows = list()

    def window_catcher(hwnd, arg):
        title = win32gui.GetWindowText(hwnd)
        if title in title_list:
            pid = win32process.GetWindowThreadProcessId(hwnd)[1]
            valid_windows.append((hwnd, title, pid))

    win32gui.EnumWindows(window_catcher, None)
    return valid_windows
