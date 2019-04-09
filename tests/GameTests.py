import unittest
from Game import *


class GameTests(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_name(self):
        self.game.display_intro()
        self.assertEqual("Obi", self.game.player_name)