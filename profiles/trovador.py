from macros.auto_buff import AutoBuff
from macros.click_spam import ClickSpam
from macros.farming import RainstormFarming
from macros.skill_spam import SkillSpam
from pynput.keyboard import Key

from macros.sp_auto_pot import SpAutoPot
from resources.buffs_code import Buffs

macros = {
    "F1 Spam": SkillSpam(Key.f1, 10),
    "Auto-Pot | SP (F9)": SpAutoPot(Key.f9, percent_sp=45),
    "Abyss3 Farm (F1,F3,F8) [End]": RainstormFarming(Key.f1, Key.f3, Key.end, 'abyss_03', arrow_pack_key=Key.f8,
                                                     delay=500),
    "Auto-Buff | Con. (F2)": AutoBuff(Key.f2, Buffs.Concentration),
    "Auto-Buff | Bragi (F4)": AutoBuff(Key.f4, Buffs.PoemOfBragi),
    "Auto-Clicker [Home]": ClickSpam(Key.home)
}
