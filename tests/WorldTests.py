import unittest

from Player import Player
from RandomEvent import *
from World import *


class WorldTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Obi")
        self.event = RandomEvent(1)
        self.world = World(self.player)

    def test_random_event_greeting(self):
        new_event = self.world.generate_random_event()
        greetings = ["Hello, there", "Greetings, traveler", "Good day, adventurer"]
        self.assertTrue(new_event.event_greeting() in greetings)
