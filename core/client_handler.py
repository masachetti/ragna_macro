from threading import Lock

import win32api
import win32con
import win32process

from utils import win32_utils


class ClientHandler:
    _instance = None
    _lock: Lock = Lock()
    _window_handler = None
    _process_handler = None

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ClientHandler, cls).__new__(cls)
        return cls._instance

    def set_window_handler(self, hwnd):
        self._window_handler = hwnd
        self._process_handler = win32_utils.get_process_handler_from_window(hwnd)

    def read_address(self, address, len):
        with self._lock:
            value = win32process.ReadProcessMemory(self._process_handler, address, len)
        return value

    def send_key_up(self, key):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_KEYUP, key, 0)

    def send_key_down(self, key):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_KEYDOWN, key, 0)

    def send_mouse_lbutton_down(self):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)

    def send_mouse_lbutton_up(self):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_LBUTTONUP, 0, 0)

    def send_mouse_rbutton_down(self):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)

    def send_mouse_rbutton_up(self):
        with self._lock:
            win32api.PostMessage(self._window_handler, win32con.WM_RBUTTONUP, 0, 0)
