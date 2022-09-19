import curses
from typing import Union, List

import pick


class WrappedPicker(pick.Picker):
    def __init__(self, key_select_callback, *args, **kwargs):
        self.callback = key_select_callback
        super().__init__(*args, **kwargs)

    def run_loop(self, screen) -> Union[List[pick.PICK_RETURN_T], pick.PICK_RETURN_T]:
        while True:
            self.draw(screen)
            c = screen.getch()
            if c in pick.KEYS_UP:
                self.move_up()
            elif c in pick.KEYS_DOWN:
                self.move_down()
            elif c in pick.KEYS_ENTER:
                return self.get_selected()
            elif c == curses.KEY_F1:
                self.callback(self.get_selected())
