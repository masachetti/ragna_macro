import win32api
import win32con
import win32gui
import win32process

WINDOW_NAME = "4th | Gepard Shield 3.0 (^-_-^)"
ACCESS_CODE = win32con.PROCESS_VM_READ


class ClientHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClientHandler, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.window_handler = get_window_handler()
        self.process_handler = get_process_handler_from_window(self.window_handler)

    def read_address(self, address, len):
        value = win32process.ReadProcessMemory(self.process_handler, address, len)
        return value

    def send_key_up(self, key):
        win32api.PostMessage(self.window_handler, win32con.WM_KEYUP, key, 0)

    def send_key_down(self, key):
        win32api.PostMessage(self.window_handler, win32con.WM_KEYDOWN, key, 0)

    def send_mouse_lbutton_down(self):
        win32api.PostMessage(self.window_handler, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)

    def send_mouse_lbutton_up(self):
        win32api.PostMessage(self.window_handler, win32con.WM_LBUTTONUP, 0, 0)

    def send_mouse_rbutton_down(self):
        win32api.PostMessage(self.window_handler, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)

    def send_mouse_rbutton_up(self):
        win32api.PostMessage(self.window_handler, win32con.WM_RBUTTONUP, 0, 0)



def get_window_handler():
    window_handler = win32gui.FindWindow(None, WINDOW_NAME)
    return window_handler


def get_process_handler_from_window(window_handler):
    if window_handler:
        pid = win32process.GetWindowThreadProcessId(window_handler)
        if pid and len(pid) >= 2:
            process_handler = win32api.OpenProcess(ACCESS_CODE, False, pid[1])
            return process_handler
