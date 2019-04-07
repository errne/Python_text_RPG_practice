from MaterialTypes import *
from Weapon import Weapon
from WeaponTypes import *


class Shop:

    def __init__(self, name):
        self.name = name
        self.weapons = self.generate_weapons_stock()

    def generate_weapons_stock(self):
        weapons_stock = []
        material_list = MaterialTypes.create_list(self)
        weapons_list = WeaponTypes.create_list(self)
        for material in material_list:
            for weapon_type in weapons_list:
                weapon = Weapon(material, weapon_type)
                weapons_stock.append(weapon)
        return weapons_stock

    def display_weapons(self):
        display_number = 0
        for weapon in self.weapons:
            display_number += 1
            print("\t " + str(display_number) + ". Buy " + weapon.to_string() + " for " + str(weapon.max_damage * 3))

    def transaction(self):
        print("Enter the number of an item you wish to buy: ")
        player_input = int(input())
        return self.weapons[player_input-1]

    def player_enter_shop(self, player):
        print("You enter " + self.name + " shop")
        print("\t Look at the list of things you can buy.")
        self.display_weapons()
        sold_item = self.transaction()
        player.buy_weapon(sold_item, sold_item.max_damage * 3)
