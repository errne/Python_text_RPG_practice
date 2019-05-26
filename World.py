import random

from Room import Room
from Shop import Shop


class World:

    def __init__(self, player):
        self.player = player
        self.traveling_is_on = True

    def display_intro(self):
        print("You hit the road!")

    def travel(self):
        while self.player.is_alive & self.traveling_is_on:
            self.generate_next_stop()
            self.will_continue()

    def generate_next_stop(self):
        random_no = random.randint(1, 3)
        if random_no == 1:
            print("You come to the shop. \n")
            self.enter_shop()
        if random_no == 2:
            print("You see an entrance to the dungeon.\n")
            self.enter_room()
        if random_no ==3:
            print ("You walk and walk and walk and nothing interesting happens")

    def generate_shop(self):
        name_list = ["Zossy's Sharpies", "Bran's Boom-Booms", "Mesmash Things", "Swords Galore", "Pick'a'Sord", "Weaponsbury"]
        name = random.choice(name_list)
        shop = Shop(name)
        return shop

    def enter_shop(self):
        print("Would you like to enter?")
        player_input = input()
        if player_input == "no":
            return
        if player_input == "yes":
           shop = self.generate_shop()
           shop.player_enter_shop(self.player)

    def generate_room(self):
        room = Room(self.player)
        return room

    def enter_room(self):
        print("Will you enter it?")
        player_input = input()
        if player_input == "no":
            return
        if player_input == "yes":
            room = self.generate_room()
            room.generate_enemies()
            room.room_fights()

    def will_continue(self):
        print("Would you like to continue your adventure?")
        player_input = input()
        if player_input == "no":
            self.traveling_is_on = False
        if player_input == "yes":
            return








