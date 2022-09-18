import time
import win32con

from core.client_handler import ClientHandler
from core.macros_monitor import MacrosMonitor
from core.memory_reader import MemoryReader
from models.macro import Macro
from resources.buffs_code import Buffs


def test_usar_skill():
    client = ClientHandler()
    time.sleep(3)
    client.send_key_down(win32con.VK_F1)
    time.sleep(0.05)
    client.send_key_up(win32con.VK_F1)
    time.sleep(0.05)
    client.send_mouse_lbutton_down()
    time.sleep(0.05)
    client.send_mouse_lbutton_up()


def test_macro_monitor():
    macro1 = Macro(name="Macro1")
    macro1.running = True
    macro2 = Macro(name="Macro2")
    macro3 = Macro(name="Macro3", hotkey='F1')

    monitor = MacrosMonitor([macro1, macro2, macro3])
    monitor.start()


def test_buff_reader():
    mem_reader = MemoryReader()
    print(mem_reader.has_buff(Buffs.CartBoost))


def test_win32api():
    import win32gui
    import win32process

    def func(hwnd, target_title):
        title = win32gui.GetWindowText(hwnd)
        if target_title == title:
            pid = win32process.GetWindowThreadProcessId(hwnd)
            print(hwnd, pid)

    win32gui.EnumWindows(func, "4th | Gepard Shield 3.0 (^-_-^)")


if __name__ == '__main__':
    test_win32api()
