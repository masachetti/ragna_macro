import time

import pynput
import win32con

from core.client_handler import ClientHandler
from macro_manager import MacroManager
from macro_pool_handler import MacroPoolHandler
from macros.macro_test import MacroTest


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


def test_macro_pool_handler():
    macro_test1 = MacroTest(pynput.keyboard.Key.f2, 2)
    macro_test2 = MacroTest(pynput.keyboard.Key.f4, "Alguma coisa aqui", 2000)
    pool = MacroPoolHandler([macro_test1, macro_test2])
    print(pool.macro_list)
    print(pool._listeners)
    print(pool._enabled_macros)
    pool.start()


def test_macro_manager():
    macro_test1 = MacroTest(pynput.keyboard.Key.f2, 2)
    macro_test2 = MacroTest(pynput.keyboard.Key.f4, "Alguma coisa aqui", 2000)
    pool = MacroManager([macro_test1, macro_test2])
    print(pool.macro_list)
    print(pool._listeners)
    pool._listeners[0].join()


if __name__ == '__main__':
    test_macro_manager()
