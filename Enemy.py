import random


class Enemy:
    maxHP = 75
    isAlive = True
    types = ["Undead", "Humanoid", "Animal"]
    namesForUndead = ["Zombie", "Vampire", "Forsaken", "Skeleton"]
    namesForAnimals = ["Cave Bear", "Cave Wolf", "Lizard", "Giant Bat"]
    namesForHumanoids = ["Warrior", "Bandit", "Warlock", "Assassin"]
    allNames = [namesForUndead, namesForHumanoids, namesForAnimals]

    def __init__(self):
        self.randomForType = random.randint(0, len(self.types) - 1)
        self.randomForName = random.randint(0, 3)
        self.type = self.types[self.randomForType]
        self.name = self.allNames[self.randomForType][self.randomForName]
        self.hp = random.randint(10, self.maxHP)
        self.maxAttackDamage = 25
        # self.attackDamage = random.randint(3, 25)
        self.armour = self.pick_armour_level()

    def hp_count(self):
        return self.hp

    def pick_armour_level(self):
        if self.randomForType == 0:
            return 5
        elif self.randomForType == 1:
            return 15
        else:
            return 3

    def deal_damage_to_player(self):
        return random.randint(3, self.maxAttackDamage)

    def receive_damage(self, received_damage):
        self.hp -= received_damage
        if self.hp < 1:
            self.isAlive = False
            self.hp = 0

    def to_string(self):
        return "You meet a " + self.name + " who has " + str(self.hp) + " hp and wants to fight you"
