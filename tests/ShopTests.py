import unittest
from Player import *
from Shop import *


class ShopTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Obi")
        self.shop = Shop("Dragonwares")

    def test_has_name(self):
        self.assertEqual("Dragonwares", self.shop.name)

    def test_weapon_stock(self):
        self.assertEqual(16, len(self.shop.weapons))

    def test_player_can_equip_weapon_from_list(self):
        self.player.equip_new_weapon(self.shop.weapons[3])
        self.assertEqual(31, self.player.max_attack_damage)