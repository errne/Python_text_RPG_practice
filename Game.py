from Player import *


class Game:

    def __init__(self):
        self.game_is_on = True
        self.player_name = ''

    def display_intro(self):
        print("Hello there, what is your name?\n")
        # self.player_name = input().capitalize()
        self.set_player_name()
        print(self.player_name + " your adventure starts here")
        print("Welcome to the dungeon!")

    def set_player_name(self):
        self.player_name = input().capitalize()

    def create_player(self, player_name):
        return Player(player_name)
