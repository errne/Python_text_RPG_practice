import unittest
from Player import *


class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Obi")

    def test_name(self):
        self.assertEqual("Obi", self.player.name)

    def test_starting_health(self):
        self.assertEqual(100, self.player.health)

    def test_can_lose_health(self):
        self.player.lose_health(15)
        self.assertEqual(85, self.player.health)

    def test_has_3_health_potions_at_start(self):
        self.assertEqual(3, self.player.numHealthPots)

    def test_health_pots_heal(self):
        for _ in range(3):
            self.player.lose_health(15)
        self.player.drink_health_potion()
        self.assertEqual(85, self.player.health)

    def test_health_pots_not_heal_when_0(self):
        for _ in range(3):
            self.player.drink_health_potion()
        self.player.lose_health(15)
        self.player.drink_health_potion()
        self.assertEqual(85, self.player.health)
        self.assertEqual(0, self.player.numHealthPots)

    def test_can_deal_damage(self):
        self.assertEqual(True, self.player.deal_damage() > 4)

    def test_can_receive_damage(self):
        self.player.take_damage(25)
        self.assertEqual(75, self.player.health)

    def test_drink_attack_potion(self):
        self.player.numAttackPots += 1
        self.player.drink_attack_potion()
        self.assertEqual(50, self.player.maxAttackDmg)

    def test_player_starts_with_0_gold(self):
        self.assertEqual(0, self.player.goldPouch)

    def test_can_add_gold(self):
        self.player.add_gold_to_pouch(25)
        self.assertEqual(25, self.player.goldPouch)


