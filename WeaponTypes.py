from enum import Enum


class WeaponTypes(Enum):
    MACE = 3
    AXE = 5
    SWORD = 7
    BATTLEAXE = 8

    def create_list(self):
        weapon_list =[]
        for material in WeaponTypes:
            weapon_list.append(material)
        return weapon_list
