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
            print(f"\t {display_number}. Buy {weapon.to_string()} for {weapon.max_damage * 3}")

    def transaction(self):
        print("what do you wish to buy: ")
        player_input = 0
        while 1 > player_input or 16 < player_input:
            try:
                player_input = int(input(f"Please enter your number between 1 and {len(self.weapons)}: \n"))
            except ValueError:
                print("That wasn't a number :(")

        return self.weapons[player_input-1]

    def player_enter_shop(self, player):
        print(f"You enter {self.name} shop")
        print("\t Look at the list of things you can buy.")
        self.display_weapons()
        print("\t Would you like to buy something?")
        player_input = input().capitalize()
        negative_answers = {"No", "N", "Noo", "Nope", "Never"}
        positive_answer = {"Yes", "Y", "Yep", "Ya", "Aha", "Always"}
        if player_input in negative_answers:
            print("Bye, come again!")
            return
        elif player_input in positive_answer:
            sold_item = self.transaction()
            player.buy_weapon(sold_item, sold_item.max_damage * 3)
        else:
            print("Simple yes or no would suffice")
