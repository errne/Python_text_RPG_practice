import unittest
from Weapon import *
from MaterialTypes import *
from WeaponTypes import *


class WeaponTests(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon(MaterialTypes.WOOD, WeaponTypes.SWORD)

    def test_max_damage(self):
        self.assertEqual(21, self.weapon.max_damage)
