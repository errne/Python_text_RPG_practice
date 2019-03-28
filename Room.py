import random
from Enemy import *
from Battle import *


class Room:

    def __init__(self, player):
        self.number_of_enemies = self.generate_number_of_enemies()
        self.enemies = []
        self.player = player
        self.treasure_chest = 0

    def generate_number_of_enemies(self):
        return random.randint(1, 3)

    def generate_enemies(self):
        number_of_enemies = self.generate_number_of_enemies()
        for enemy in range(0, number_of_enemies):
            enemy = Enemy()
            self.enemies.append(enemy)

    def add_gold_to_treasure_chest(self):
        amount_to_add = random.randint(10, 25)
        self.treasure_chest += amount_to_add

    def loot_treasure_chest(self):
        self.player.add_gold_to_pouch(self.treasure_chest)
        print("# You found " + str(self.treasure_chest) + " gold in treasure chest. #")
        print("# Now you have " + str(self.player.goldPouch) + " gold in your pouch. #")
        self.treasure_chest = 0

    def room_fights(self):
        for enemy in self.enemies:
            print(enemy.to_string())
            battle = Battle(self.player, enemy)
            battle.fight()
            if enemy.hp < 1:
                self.add_gold_to_treasure_chest()
        self.loot_treasure_chest()



