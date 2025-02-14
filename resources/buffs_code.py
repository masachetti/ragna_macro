class Buffs:
    Arrows = 695
    CartBoost = 461
    Concentration = 3
    PoemOfBragi = 72

    PRM_RisingWings = 188
    PRM_AgiUp = 12
    PRM_WeaponBlocking = 337
    PRM_DualCast = 186
    PRM_AutoGuard = 58
    PRM_MagicPierce = 340
    PRM_Kimi = 1303

    @staticmethod
    def get_buff_by_id(buff_id: int):
        if isinstance(buff_id, int):
            for key, value in Buffs.__dict__:
                if value == buff_id:
                    return key
        return None
