import random

import self as self

from Enemy import *
from Player import *
from Game import *
from Battle import *
from Room import *



game = Game()

game.display_intro()
player = game.create_player(game.player_name)

# player = Player(player_name)
# enemy = Enemy()
#
# print(enemy.to_string())
# print(player.name, player.health)
#
# battle = Battle(player, enemy)
# battle.fight()

room = Room(player)
room.generate_enemies()
room.room_fights()

room = Room(player)
room.generate_enemies()
room.room_fights()

