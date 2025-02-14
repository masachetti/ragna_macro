import curses
from threading import Lock

from core.memory_reader import MemoryReader

ABORT_KEYS = [curses.KEY_END]
COLOR_TRUE_CONDITION_TIP = 1
COLOR_FALSE_CONDITION_TIP = 2
COLOR_TRUE_CONDITION = 3
COLOR_FALSE_CONDITION = 4


def config_curses():
    try:
        # use the default colors of the terminal
        # curses.use_default_colors()
        # hide the cursor
        curses.curs_set(0)
        curses.init_pair(COLOR_TRUE_CONDITION_TIP, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(COLOR_FALSE_CONDITION_TIP, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(COLOR_TRUE_CONDITION, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(COLOR_FALSE_CONDITION, curses.COLOR_RED, curses.COLOR_BLACK)
    except:
        # Curses failed to initialize color support, eg. when TERM=vt100
        curses.initscr()


class BuffCodeMonitor:
    _instance = None
    _lock: Lock = Lock()
    reader =  MemoryReader()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(BuffCodeMonitor, cls).__new__(cls)
        return cls._instance

    def draw(self, screen):
        screen.clear()
        screen.nodelay(1)

        x, y = 1, 1  # start point
        max_y, max_x = screen.getmaxyx()
        max_rows = max_y - y  # the max rows we can draw

        buff_codes = self.reader.buffs_array()[:20]

        for code in buff_codes:
            screen.addnstr(y,x, f'{code}', max_x - 2)
            y += 1

        screen.refresh()

    def run_loop(self, screen):
        while True:
            self.draw(screen)
            c = screen.getch()
            if c in ABORT_KEYS:
                break

    def _start(self, screen):
        config_curses()
        self.run_loop(screen)

    def join(self):
        curses.wrapper(self._start)
