
from Game import *

game = Game()
player = game.display_intro()

if player is None:
    player = game.create_player(game.player_name)

# player.add_gold_to_pouch(1000)

game.enter_world(player)

