import time

from core.client_handler import ClientHandler
from utils import convert_pynput_key_to_virtual_key


def click_key(key):
    vk = convert_pynput_key_to_virtual_key(key)
    client = ClientHandler()
    client.send_key_down(vk)
    time.sleep(0.02)
    client.send_key_up(vk)
    time.sleep(0.02)


def click_mouse_lbutton():
    client = ClientHandler()
    client.send_mouse_lbutton_down()
    time.sleep(0.02)
    client.send_mouse_lbutton_up()
    time.sleep(0.02)


def click_mouse_rbutton():
    client = ClientHandler()
    client.send_mouse_rbutton_down()
    time.sleep(0.02)
    client.send_mouse_rbutton_up()
    time.sleep(0.02)
