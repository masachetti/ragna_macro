import time

import win32con

from client_handler import ClientHandler


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

if __name__ == '__main__':
    test_usar_skill()