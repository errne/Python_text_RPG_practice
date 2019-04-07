from MaterialTypes import *
from Weapon import Weapon
from WeaponTypes import *


class Shop:

    def __init__(self, name):
        self.name = name
        self.weapons = self.generate_weapons_stock()

    def generate_weapons_stock(self):
        weapons_stock = []
        material_list = MaterialTypes.create_list()
        weapons_list = WeaponTypes.create_list()
        for material in material_list:
            for weapon_type in weapons_list:
                weapon = Weapon(material, weapon_type)
                weapons_stock.append(weapon)
        return weapons_stock
