import unittest
from Enemy import *


class EnemyTests(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy()

    def test_name(self):
        self.assertEqual(True, len(self.enemy.name) > 3)

    def test_hp_is_above_9(self):
        self.assertEqual(True, self.enemy.hp_count() > 9)

    def test_has_type(self):
        self.assertEqual(True, len(self.enemy.type) > 5)

    def test_random(self):
        self.assertEqual(True, self.enemy.randomForType < 3)

    def test_attack_damage(self):
        self.assertEqual(True, self.enemy.attackDamage >= 3 & self.enemy.attackDamage < 26)

    def test_armour_level_above_2(self):
        self.assertEqual(True, self.enemy.armour > 2)
