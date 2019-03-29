import random


class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.battle_is_on = True
        self.health_potion_drop_chance = 95
        self.attack_potion_drop_chance = 25

    def fight(self):

        while self.battle_is_on:
            print("\tYour HP: " + str(self.player.health))
            print("\t" + self.enemy.name + "'s HP: " + str(self.enemy.hp))
            print("\n\tWhat would you like to do?")
            print("\t1. Attack")
            print("\t2. Drink health potion")
            print("\t3. Flee")
            player_input = input()

            if player_input == "1":
                self.attack_choice()

            elif player_input == "2":
                self.player.drink_health_potion()
                print("\t> You now have" + str(self.player.health) + " HP." + "\n\t> You now have " +
                      str(self.player.num_health_pots) + " health potions left.\n")

            elif player_input == "3":
                print("\t> You run away from the " + self.enemy.name)
                self.battle_is_on = False
                return

            else:
                print("\tInvalid command")

        self.aftermath()

    def loot_drop(self):
        if random.randint(1, 100) < self.health_potion_drop_chance:
            print(" # The " + self.enemy.name + " dropped a health potion. # ")
            self.player.num_health_pots += 1
            print(" # You now have " + str(self.player.num_health_pots) + " health potion(s). # ")

        if random.randint(1, 100) < self.attack_potion_drop_chance:
            print(" # The " + self.enemy.name + " dropped a attack potion. # ")
            self.player.num_attack_pots += 1
            print(" # You now have " + str(self.player.num_attack_pots) + " attack potion(s). # ")

    def attack_choice(self):
        damage_calculation = self.player.deal_damage() - self.enemy.armour
        damage_dealt = max(0, damage_calculation)
        self.enemy.receive_damage(damage_dealt)
        damage_taken = self.enemy.deal_damage_to_player()
        self.player.take_damage(damage_taken)

        print("\t> You strike the " + self.enemy.name + " for " + str(damage_dealt) + " damage")
        print("\t> You received " + str(damage_taken) + " in retaliation")

        if not self.player.is_alive:
            print("\t You have taken too much damage, you are too weak to go on")
            self.battle_is_on = False

        if not self.enemy.is_alive:
            self.battle_is_on = False

    def aftermath(self):
        if self.player.health < 1:
            print("\t> You have been defeated")

        elif self.enemy.hp < 1:
            print(" # " + self.enemy.name + " was defeated! # ")
            print((" # You have " + str(self.player.health) + "HP left # "))
            self.loot_drop()

        else:
            print("\t> You fled the battle you coward")
