from pynput.keyboard import Key, KeyCode

from macros.auto_buff import AutoBuff
from macros.auto_buff_with_multiple_keys import AutoBuffWithMultipleKeys
from macros.prm_manual_swap import PRMManualSwap
from macros.skill_rotation import SkillRotation
from resources.buffs_code import Buffs

macros = {
    "Petals Rotation [X]": SkillRotation(KeyCode.from_char('x'), [Key.f2, Key.f3, Key.f4, Key.f5]),
    "Petals and Bolt [C]": SkillRotation(KeyCode.from_char('c'), [Key.f2,'Q', Key.f3, 'W', Key.f4, 'E', Key.f5, 'R']),

    "Auto-Buff | Dual Cast (F8)": AutoBuff(Key.f8, Buffs.PRM_DualCast),
    "Auto-Buff | Auto Guard (4)": AutoBuff('4', Buffs.PRM_AutoGuard),
    # "Auto-Buff | Agi Up (3)": AutoBuff('3', Buffs.PRM_AgiUp),
    "Teleport": PRMManualSwap(KeyCode.from_char('z'), 'Y', '6', 'I'),
    "Auto-Buff | Agi Up": AutoBuffWithMultipleKeys(['O', '3', 'I'], Buffs.PRM_AgiUp),
}

