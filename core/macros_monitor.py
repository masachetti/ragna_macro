"""
Ideia:

Apresentar as macros em duas categorias
Triggered Macros e Not triggered macros
(Obviamente Always Triggered sempre ficarão em Triggered)
Nas triggered macros, as macros com condicional valido ficam em verde
As com condicional invalido ficam em laranja
Colocar a hotkey entre parentenses depois do nome da macro
"""
import curses
from dataclasses import dataclass
from typing import List

from models.macro import Macro

ABORT_KEYS = [curses.KEY_END]

@dataclass
class MacrosMonitor:
    macros: List[Macro]

    def get_lines(self):
        lines: List[str] = []
        for macro in self.macros:
            hk = macro.hotkey
            lines.append(f"{macro.name} ({hk if hk else '-'})")
        return lines

    def draw(self, screen):
        screen.clear()

        x, y = 1, 1  # start point
        max_y, max_x = screen.getmaxyx()
        max_rows = max_y - y  # the max rows we can draw

        lines = self.get_lines()

        lines_to_draw = lines[:max_rows]

        for line in lines_to_draw:
            screen.addnstr(y, x, line, max_x - 2)
            y += 1

        screen.refresh()

    def run_loop(self, screen):
        while True:
            self.draw(screen)
            c = screen.getch()
            if c in ABORT_KEYS:
                break

    def config_curses(self):
        try:
            # use the default colors of the terminal
            curses.use_default_colors()
            # hide the cursor
            curses.curs_set(0)
        except:
            # Curses failed to initialize color support, eg. when TERM=vt100
            curses.initscr()

    def _start(self, screen):
        self.config_curses()
        self.run_loop(screen)

    def start(self):
        curses.wrapper(self._start)
