import random

from ArmourTypes import ArmourTypes
from Weapon import *
from MaterialTypes import *
from WeaponTypes import *


class Player:
    base_attack_damage = 10
    num_health_pots = 3
    num_attack_pots = 0
    gold_pouch = 0
    inventory = {}
    is_alive = True

    def __init__(self, name):
        self.__health = 100
        self.__armour_slots = {"Helm": None, "Chest": None, "Trousers": None, "Boots": None}
        self.name = name
        self.weapon = Weapon(MaterialTypes.WOOD, WeaponTypes.SWORD)
        self.max_attack_damage = self.base_attack_damage + self.weapon.max_damage

    def get_health(self):
        return self.__health

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
        self.__health += 30
        if self.__health > 100:
            self.__health = 100

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
        damage_received_with_armour = damage_received - self.armour_protection_value()
        if damage_received_with_armour < 1:
            damage_received_with_armour = 0
        self.__health -= damage_received_with_armour
        if self.__health < 1:
            self.is_alive = False
            self.__health = 0

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

    def equip_new_armour(self, armour):
        if armour.armour_type == ArmourTypes.BOOTS:
            self.__armour_slots["Boots"] = armour
        elif armour.armour_type == ArmourTypes.HELM:
            self.__armour_slots["Helm"] = armour
        elif armour.armour_type == ArmourTypes.TROUSERS:
            self.__armour_slots["Trousers"] = armour
        elif armour.armour_type == ArmourTypes.CHEST:
            self.__armour_slots["Chest"] = armour

    def get_total_armour_level(self):
        total_armour_value = 0
        for armour in self.__armour_slots:
            if self.__armour_slots[armour] is not None:
                total_armour_value += self.__armour_slots[armour].armour_level
        return total_armour_value

    def armour_protection_value(self):
        armour_protection = self.get_total_armour_level()
        return armour_protection // 3

    # def add_item_to_inventory(self, new_item):
    #     for item in self.inventory:
    #         if item.to_string() == new_item.to_string():
    #             self.inventory[item] += 1

    # self.inventory[new_item] = 1
