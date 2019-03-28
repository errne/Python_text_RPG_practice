import random


class Player:
    health = 100
    maxAttackDmg = 45
    numHealthPots = 3
    numAttackPots = 0
    attackPotionBoost = 5
    attackPotionDropChance = 20
    healthPotionHealAmount = 30
    healthPotionDropChance = 40
    goldPouch = 0

    def __init__(self, name):
        self.name = name

    def lose_health(self, damage_received):
        self.health -= damage_received

    def drink_health_potion(self):
        if self.numHealthPots > 0:
            self.health_potion_heal()
            self.numHealthPots -= 1
            if self.numHealthPots <= 0:
                self.numHealthPots = 0
        else:
            print("\t> You do not have any health potions, defeat enemies for a chance to get one")

    def health_potion_heal(self):
        self.health += self.healthPotionHealAmount
        if self.health > 100:
            self.health = 100

    def drink_attack_potion(self):
        if self.numAttackPots > 0:
            self.attack_potion_boost()
            self.numAttackPots -= 1
            if self.numAttackPots <= 0:
                self.numAttackPots = 0
        else:
            print("\t> You do not have any attack potions, defeat enemies for a chance to get one")

    def attack_potion_boost(self):
        self.maxAttackDmg += self.attackPotionBoost
        if self.maxAttackDmg > 75:
            self.health = 75
            print("Your maximum damage cannot go any higher")

    def deal_damage(self):
        return random.randint(5, self.maxAttackDmg)

    def take_damage(self, damage_received):
        self.health -= damage_received

    def add_gold_to_pouch(self, amount_of_gold):
        self.goldPouch += amount_of_gold


