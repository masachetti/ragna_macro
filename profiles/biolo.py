from pynput.keyboard import Key

from macros.auto_buff import AutoBuff
from macros.click_spam import ClickSpam
from macros.hp_auto_pot import HpAutoPot
from macros.skill_spam import SkillSpam
from resources.buffs_code import Buffs

macros = {
    "Skill Spam [F1]": SkillSpam(Key.f1, 10),
    "Auto-Pot | Hp (F9)": HpAutoPot(Key.f9, percent_hp=60),
    "Auto-Buff | Cart Boost (F)": AutoBuff(Key.f2, Buffs.CartBoost),
    "Auto-Clicker [Home]": ClickSpam(Key.home)
}

