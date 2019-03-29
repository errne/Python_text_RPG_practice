import random


class Player:
    health = 100
    max_attack_damage = 45
    num_health_pots = 3
    num_attack_pots = 0
    gold_pouch = 0
    is_alive = True

    def __init__(self, name):
        self.name = name

    def drink_health_potion(self):
        if self.num_health_pots > 0:
            self.health_potion_heal()
            self.num_health_pots -= 1
            if self.num_health_pots <= 0:
                self.num_health_pots = 0
        else:
            print("\t> You do not have any health potions, defeat enemies for a chance to get one")

    def health_potion_heal(self):
        self.health += 30
        if self.health > 100:
            self.health = 100

    def drink_attack_potion(self):
        if self.num_attack_pots > 0:
            self.attack_potion_boost()
            self.num_attack_pots -= 1
            if self.num_attack_pots <= 0:
                self.num_attack_pots = 0
        else:
            print("\t> You do not have any attack potions, defeat enemies for a chance to get one")

    def attack_potion_boost(self):
        self.max_attack_damage += 5
        if self.max_attack_damage > 75:
            self.health = 75
            print("Your maximum damage cannot go any higher")

    def deal_damage(self):
        return random.randint(5, self.max_attack_damage)

    def take_damage(self, damage_received):
        self.health -= damage_received
        if self.health < 1:
            self.is_alive = False
            self.health = 0

    def add_gold_to_pouch(self, amount_of_gold):
        self.gold_pouch += amount_of_gold


