from macros.auto_pot import AutoPot
from macros.farming import RainstormFarming
from macros.skill_spam import SkillSpam
from pynput import keyboard

macros = [
    SkillSpam(keyboard.Key.f1, 10),
    AutoPot(keyboard.Key.f9),
    RainstormFarming(keyboard.Key.f1, keyboard.Key.f3, keyboard.Key.end, 'abyss_03')
]