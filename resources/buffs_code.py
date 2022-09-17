class Buffs:
    Arrows = 695
    CartBoost = 461
    Concentration = 3
    PoemOfBragi = 72

    @staticmethod
    def get_buff_by_id(buff_id: int):
        if isinstance(buff_id, int):
            for key, value in Buffs.__dict__:
                if value == buff_id:
                    return key
        return None
