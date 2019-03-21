class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        while self.enemy.hp > 0:
            print("\tYour HP: " + str(self.player.health))
            print("\t" + self.enemy.name + "'s HP: " + str(self.enemy.hp))
            print("\n\tWhat would you like to do?")
            print("\t1. Attack")
            print("\t2. Drink health potion")
            print("\t3. Flee")
            player_input = input()

            if player_input == "1":
                damage_calculation = self.player.deal_damage() - self.enemy.armour
                damage_dealt = max(0, damage_calculation)
                self.enemy.hp -= damage_dealt
                damage_taken = self.enemy.deal_damage_to_player()
                self.player.health -= damage_taken

                print("\t> You strike the " + self.enemy.name + " for " + str(damage_dealt) + " damage")
                print("\t> You received " + str(damage_taken) + " in retaliation")

                if self.player.health < 1:
                    print("\t You have taken too much damage, you are too weak to go on")
                    return

            elif player_input == "2":
                self.player.drink_health_potion()
                print("\t> You drank a health potion, healed for: " + str(self.player.healthPotionHealAmount) + "."
                      + "\n\t> You now have" + str(self.player.health) + " HP." + "\n\t> You now have " +
                      str(self.player.numHealthPots) + " health potions left.\n")

            elif player_input == "3":
                print("\t> You run away from the " + self.enemy.name)

            else:
                print("\tInvalid command")
