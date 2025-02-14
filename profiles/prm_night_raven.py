from pynput.keyboard import Key, KeyCode

from macros.auto_buff import AutoBuff
from macros.auto_buff_with_multiple_keys import AutoBuffWithMultipleKeys
from macros.skill_rotation import SkillRotation
from resources.buffs_code import Buffs

macros = {
    "Auto-Buff | Rising Wings (F4)": AutoBuff(Key.f4, Buffs.PRM_RisingWings),
    "Auto-Buff | Weapon Blocking (F5)": AutoBuff(Key.f5, Buffs.PRM_WeaponBlocking),

    # Nessa macro, passar em ordem quais Keys usar para aplicar o buff
    # Por exemplo, Colocar Manual (A) -> Buffar (S) -> Colocar outro manual (D)
    "Auto-Buff | Agi Up (A-S-D)": AutoBuffWithMultipleKeys(['A', 'S', 'D'], Buffs.PRM_AgiUp),
}

