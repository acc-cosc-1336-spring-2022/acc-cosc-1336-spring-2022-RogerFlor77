import random

class Die:

    def _init_(self, sides_count = 6):
        self.sides_count = sides_count

    def roll(self):
        __roll_value = random.randint(1, self.sides_count)
        return __roll_value

        def get_roll_value(self):
            return self.roll()
        def _str_(self):
            return str("The Rolled Value is {0}".
    format(self.get_roll_value()))


def dice_time():
    die = Die()
    decision = "n"
    decision = input("Do you wan to roll the dice? y/n")
    while decision.lower() == "y":
        die.roll()
        print(die)
        decision = input("Do you want to roll the dice again? y/n")
    while decision.lower() == "n":
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid Input. y or no")
        dice_time()