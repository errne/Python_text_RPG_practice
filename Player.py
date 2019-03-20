class Player:
    health = 100
    attackDmg = 45
    numHealthPots = 3
    numAttackPots = 0
    attackPotionBoost = 5
    attackPotionDropChance = 20
    healthPotionHealAmount = 30
    healthPotionDropChance = 40

    def __init__(self, name):
        self.name = name

    def lose_health(self, damage_received):
        self.health -= damage_received
