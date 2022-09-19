from typing import List

import win32api
import win32con
import win32gui
import win32process

ACCESS_CODE = win32con.PROCESS_VM_READ


def get_windows_with_valid_title(title_list: List[str]):
    valid_windows = list()

    def window_catcher(hwnd, arg):
        title = win32gui.GetWindowText(hwnd)
        if title in title_list:
            pid = win32process.GetWindowThreadProcessId(hwnd)[1]
            valid_windows.append((hwnd, title, pid))

    win32gui.EnumWindows(window_catcher, None)
    return valid_windows


def flash_and_bring_the_window_to_top(hwnd):
    win32gui.FlashWindow(hwnd, 1)
    win32gui.BringWindowToTop(hwnd)


def get_process_handler_from_window(window_handler):
    if window_handler:
        pid = win32process.GetWindowThreadProcessId(window_handler)
        if pid and len(pid) >= 2:
            process_handler = win32api.OpenProcess(ACCESS_CODE, False, pid[1])
            return process_handler
