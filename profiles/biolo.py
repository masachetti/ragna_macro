from pynput.keyboard import Key

from macros.auto_buff import AutoBuff
from macros.hp_auto_pot import HpAutoPot
from macros.skill_spam import SkillSpam
from resources.buffs_code import Buffs

macros = [
    SkillSpam(Key.f1, 10),
    HpAutoPot(Key.f9, percent_hp=60),
    AutoBuff(Key.f2, Buffs.CartBoost),
]
