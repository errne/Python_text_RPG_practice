from random import random


class RandomEvent:
    greetings = ["Hello, there", "Greetings, traveler", "Good day, adventurer"]

    def __init__(self, seed):
        self.seed = seed

    def event_greeting(self):
        return self.greetings[self.seed]
