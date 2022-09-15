from macros.auto_pot import AutoPot
from macros.skill_spam import SkillSpam
from pynput import keyboard

macros = [
    SkillSpam(keyboard.Key.f1, 10),
    AutoPot(keyboard.Key.f9)
]