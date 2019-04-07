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

player.add_gold_to_pouch(1000)

shop = Shop("Testor")
shop.player_enter_shop(player)
room = Room(player)
room.generate_enemies()
room.room_fights()

room = Room(player)
room.generate_enemies()
room.room_fights()

