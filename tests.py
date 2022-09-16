import time

import pynput
import win32con

from core.client_handler import ClientHandler

from core.macros_monitor import MacrosMonitor
from macros.macro_test import MacroTest
from models.macro import Macro


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
    macro2 = Macro(name="Macro2")
    macro3 = Macro(name="Macro3", hotkey='F1')

    monitor = MacrosMonitor([macro1, macro2, macro3])
    monitor.start()

if __name__ == '__main__':
    test_macro_monitor()
