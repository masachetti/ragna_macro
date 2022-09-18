from macros.auto_buff import AutoBuff
from macros.farming import RainstormFarming
from macros.skill_spam import SkillSpam
from pynput.keyboard import Key

from macros.sp_auto_pot import SpAutoPot
from resources.buffs_code import Buffs

macros = [
    SkillSpam(Key.f1, 10),
    SpAutoPot(Key.f9, percent_sp=45),
    RainstormFarming(Key.f1, Key.f3, Key.end, 'abyss_03', arrow_pack_key=Key.f8, delay=500),
    AutoBuff(Key.f2, Buffs.Concentration),
    AutoBuff(Key.f4, Buffs.PoemOfBragi),
]