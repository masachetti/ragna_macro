from threading import Lock

from pynput import keyboard


class HotkeyListener:
    # Singleton
    _instance = None
    _lock: Lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(HotkeyListener, cls).__new__(cls)
                cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.listener: keyboard.Listener = None
        self.pressed_keys = list()
        self._observers = list()

    def start(self):
        if self.listener is None:
            self.listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)
            self.listener.start()

    def on_press(self, key):
        if key not in self.pressed_keys:
            self.pressed_keys.append(key)
            self.notify()

    def on_release(self, key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)
            self.notify()

    def notify(self):
        for observer_callback in self._observers:
            try:
                observer_callback(self.pressed_keys)
            except Exception as e:
                print(e)

    def attach_observer(self, observer_callback):
        self._observers.append(observer_callback)


if __name__ == '__main__':
    watcher = HotkeyListener()
    watcher.attach_observer(lambda x: print(f"Pressed keys: {x}"))
    watcher.start()