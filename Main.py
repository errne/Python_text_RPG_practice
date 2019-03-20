import random
from Enemy import *
from Player import *




def displayIntro():
    print("Hello there, what is your name?\n")
    player_name = input().capitalize()
    print(player_name + " your adventure starts here")
    print("Welcome to the dungeon!")


gameIsOn = True

displayIntro()
enemy = Enemy()


print(enemy.to_string())
