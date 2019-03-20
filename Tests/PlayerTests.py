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