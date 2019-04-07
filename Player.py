import random
from Weapon import *
from MaterialTypes import *
from WeaponTypes import *


class Player:
    health = 100
    base_attack_damage = 10
    num_health_pots = 3
    num_attack_pots = 0
    gold_pouch = 0
    is_alive = True

    def __init__(self, name):
        self.name = name
        self.weapon = Weapon(MaterialTypes.WOOD, WeaponTypes.SWORD)
        self.max_attack_damage = self.base_attack_damage + self.weapon.max_damage

    def set_max_attack_damage(self):
        self.max_attack_damage = self.base_attack_damage + self.weapon.max_damage

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
        self.base_attack_damage += 5
        if self.base_attack_damage > 45:
            self.base_attack_damage = 45
            print("Your maximum damage cannot go any higher")
        self.set_max_attack_damage()

    def deal_damage(self):
        return random.randint(5, self.max_attack_damage)

    def take_damage(self, damage_received):
        self.health -= damage_received
        if self.health < 1:
            self.is_alive = False
            self.health = 0

    def add_gold_to_pouch(self, amount_of_gold):
        self.gold_pouch += amount_of_gold

    def buy_weapon(self, weapon, price):
        if price <= self.gold_pouch:
            self.gold_pouch -= price
            self.equip_new_weapon(weapon)
        else:
            print("You do not have enough gold for this purchase")
            return

    def equip_new_weapon(self, weapon):
        self.weapon = weapon
        self.set_max_attack_damage()
        print("You have equipped " + self.weapon.to_string())


