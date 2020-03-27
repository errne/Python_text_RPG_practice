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

    def transaction(self, limit):
        player_input = 0
        while 1 > player_input or limit < player_input:
            try:
                player_input = int(input(f"Please enter your number between 1 and {limit}: \n"))
            except ValueError:
                print("That wasn't a number :(")
        return player_input-1

    def player_buying(self, player):
        print(f"You enter {self.name} shop")
        print("\t Look at the list of things you can buy.")
        self.display_weapons()
        print("\t Would you like to buy something?")
        player_input = input().capitalize()
        negative_answers = {"No", "N", "Noo", "Nope", "Never"}
        positive_answer = {"Yes", "Y", "Yep", "Ya", "Aha", "Always"}
        if player_input in negative_answers:
            print("Maybe next time.")
            return
        elif player_input in positive_answer:
            print("What do you wish to buy? ")
            limit = len(self.weapons)
            sold_item = self.weapons[self.transaction(limit)]
            player.buy_weapon(sold_item, sold_item.max_damage * 3)
        else:
            print("Simple yes or no would suffice")

    def player_selling_all(self, player):
        player.sell_all_inventory()

    def player_selling(self, player):
        print("Which item would you like to sell?")
        item_list = player.inventory
        item_number = 0
        for item in item_list:
            item_number += 1
            print(f"\t {item_number}. Sell {item.to_string()} fo {item.price}")
        limit = len(player.inventory)
        self.player_selling_particular_item(self.transaction(limit), player)

    def player_selling_particular_item(self, item_number, player):
        print(f"You sold {player.inventory[item_number].to_string()} for {player.inventory[item_number].price}.")
        player.add_gold_to_pouch(player.inventory[item_number].price)
        player.inventory.pop(item_number)
        print(f"\t Now you have {player.gold_pouch} gold")

    def player_in_shop(self, player):
        print(f"You enter {self.name} shop")
        print("Welcome how can I help?")
        print("\t 1. Would you like to see the stock?")
        print("\t 2. Would you like to sell something?")
        print("\t 3. Would you like to sell everything?")
        print("\t 4. Would you like leave the shop?")

        player_input = input()

        if player_input == "1":
            self.player_buying(player)

        elif player_input == "2":
            self.player_selling(player)

        elif player_input == "3":
            self.player_selling_all(player)

        elif player_input == "4":
            return

        else:
            print("What was that?")
