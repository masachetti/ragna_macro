from pynput.keyboard import Key, KeyCode

from macros.auto_buff import AutoBuff
from macros.skill_rotation import SkillRotation
from resources.buffs_code import Buffs

macros = {
    "Petals Rotation [F1]": SkillRotation(KeyCode.from_char('e'), [Key.f2, Key.f3, Key.f4, Key.f5], 10),
    "Auto-Buff | Dual Cast (F8)": AutoBuff(Key.f8, Buffs.PRM_DualCast),
    "Auto-Buff | Auto Guard (4)": AutoBuff('4', Buffs.PRM_AutoGuard),
    "Auto-Buff | Agi Up (3)": AutoBuff('3', Buffs.PRM_AgiUp),

}

