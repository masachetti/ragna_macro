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
from typing import List, Union, Tuple

from models.macro import Macro

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


def create_macro_repr(macro: Macro) -> str:
    hk = macro.hotkey
    return f"{macro.name} ({hk if hk else '-'})"


@dataclass
class MacrosMonitor:
    macros: List[Macro]

    def get_triggered_macros(self):
        return [(create_macro_repr(macro), 4 - int(macro.action_condition)) for macro in self.macros if macro.running]

    def get_not_triggered_macros(self):
        return [create_macro_repr(macro) for macro in self.macros if not macro.running]

    def get_lines(self):
        lines: List[Union[str, Tuple[str, int]]] = ["--- Triggered Macros ---"]
        lines.extend(self.get_triggered_macros())
        lines.append('')
        lines.append("--- Not Triggered Macros ---")
        lines.extend(self.get_not_triggered_macros())
        return lines

    def draw(self, screen):
        screen.clear()

        x, y = 1, 1  # start point
        max_y, max_x = screen.getmaxyx()
        max_rows = max_y - y  # the max rows we can draw

        true_condition_str = "CONDITION = True"
        screen.addstr(y, x, true_condition_str, curses.color_pair(COLOR_TRUE_CONDITION_TIP))
        screen.addstr(y, x + len(true_condition_str) + 5, "CONDITION = False",
                      curses.color_pair(COLOR_FALSE_CONDITION_TIP))
        y += 2

        lines = self.get_lines()
        lines_to_draw = lines[:max_rows - 2]

        for line in lines_to_draw:
            if isinstance(line, str):
                screen.addnstr(y, x, line, max_x - 2)
            elif isinstance(line, tuple):
                screen.addnstr(y, x, line[0], max_x - 2, curses.color_pair(line[1]))
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

    def start(self):
        curses.wrapper(self._start)
