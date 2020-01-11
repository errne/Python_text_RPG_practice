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
        if self.player.is_alive:
            self.player.add_gold_to_pouch(self.treasure_chest)
            print(f"# You found {self.treasure_chest} gold in treasure chest. #")
            print(f"# Now you have {self.player.gold_pouch} gold in your pouch. #")
            self.treasure_chest = 0

    def room_fights(self):
        for enemy in self.enemies:
            print(enemy.to_string())
            battle = Battle(self.player, enemy)
            battle.fight()
            if not self.player.is_alive:
                break
            if enemy.hp < 1:
                self.add_gold_to_treasure_chest()
            self.after_fight()
        self.loot_treasure_chest()

    def after_fight(self):
        print(f"\tYour HP: {self.player.get_health()}")
        print("\n\tWhat would you like to do?")
        print("\t1. Continue")
        print("\t2. Drink health potion")
        print("\t3. Drink attack potion")
        print("\t4. Flee")
        player_input = input()

        if player_input == "1":
            return

        elif player_input == "2":
            self.player.drink_health_potion()
            print(f"\t> You now have {self.player.get_health()} HP. \n\t> You now have {self.player.num_health_pots}"
                  f" health potions left.\n")

        elif player_input == "3":
            self.player.drink_attack_potion()
            print(f"\t> You now have {self.player.num_attack_pots} attack potions left.\n")

        elif player_input == "4":
            print("\t> You run away")
            self.battle_is_on = False
            return

        else:
            print("\tInvalid command")
