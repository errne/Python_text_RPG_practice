import unittest
from Player import *


class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Obi")
        self.new_weapon = Weapon(MaterialTypes.STEEL, WeaponTypes.BATTLEAXE)

    def test_name(self):
        self.assertEqual("Obi", self.player.name)

    def test_starting_health(self):
        self.assertEqual(100, self.player.health)

    def test_has_3_health_potions_at_start(self):
        self.assertEqual(3, self.player.num_health_pots)

    def test_health_pots_heal(self):
        for _ in range(3):
            self.player.take_damage(15)
        self.player.drink_health_potion()
        self.assertEqual(85, self.player.health)

    def test_health_pots_not_heal_when_0(self):
        for _ in range(3):
            self.player.drink_health_potion()
        self.player.take_damage(15)
        self.player.drink_health_potion()
        self.assertEqual(85, self.player.health)
        self.assertEqual(0, self.player.num_health_pots)

    def test_can_deal_damage(self):
        self.assertEqual(True, self.player.deal_damage() > 4)

    def test_can_receive_damage(self):
        self.player.take_damage(25)
        self.assertEqual(75, self.player.health)

    def test_drink_attack_potion(self):
        self.player.num_attack_pots += 1
        self.player.drink_attack_potion()
        self.assertEqual(15, self.player.base_attack_damage)
        self.assertEqual(33, self.player.max_attack_damage)

    def test_drink_attack_potion__over_limit(self):
        self.player.num_attack_pots += 10
        for _ in range(9):
            self.player.drink_attack_potion()
        self.assertEqual(45, self.player.base_attack_damage)
        self.assertEqual(63, self.player.max_attack_damage)

    def test_player_starts_with_0_gold(self):
        self.assertEqual(0, self.player.gold_pouch)

    def test_can_add_gold(self):
        self.player.add_gold_to_pouch(25)
        self.assertEqual(25, self.player.gold_pouch)

    def test_player_dies(self):
        self.player.take_damage(125)
        self.assertEqual(False, self.player.is_alive)

    def test_can_equip_new_weapon(self):
        self.player.equip_new_weapon(self.new_weapon)
        self.assertEqual(66, self.player.max_attack_damage)

    def test_buy_new_weapon(self):
        self.player.add_gold_to_pouch(78)
        self.player.buy_weapon(self.new_weapon, 75)
        self.assertEqual(66, self.player.max_attack_damage)
        self.assertEqual(3, self.player.gold_pouch)




