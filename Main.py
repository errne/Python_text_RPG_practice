import random

import self as self

from Enemy import *
from Player import *
from Game import *
from Battle import *
from Room import *
from Shop import *



game = Game()

game.display_intro()
player = game.create_player(game.player_name)

shop = Shop("Testor")
shop.generate_weapons_stock()
room = Room(player)
room.generate_enemies()
room.room_fights()

room = Room(player)
room.generate_enemies()
room.room_fights()

