import random


class RandomEvent:
    greetings = ["Hello, there", "Greetings, traveler", "Good day, adventurer"]

    def __init__(self, seed, player):
        self.seed = seed
        self.player = player

    def event_greeting(self):
        return self.greetings[self.seed]

    def event_task(self):
        print("Answer this question please and you'll be rewarded.")
        questionno1 = random.randint(5, 13)
        questionno2 = random.randint(5, 13)
        print(f"what is {questionno1} times {questionno2}?")
        player_input = int(input())
        correct_answer = questionno1 * questionno2
        if player_input == correct_answer:
            self.player.add_gold_to_pouch(25)
            print("Correct. Your wisdom deserves some gold.")
            print("25 gold coins were added to your pouch")
        else:
            print("Incorrect, bye")
