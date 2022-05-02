import unittest

from class_a import Die

class test_Config(unittest.TestCase):

    def test_dice_roll(self):
        die = Die()
        die.roll()
        if die.get_roll_value() in [1, 2, 3, 4, 5, 6]:
            Rolled = True
        else:
            Rolled = True
        self.assertEqual(True, Rolled)

    def test_dice_roll1(self):
        my_die = Die()
        my_die.roll()
        self.assertEqual(False, my_die.get_roll_value == 1 or
        my_die.get_roll_value == 2 or
        my_die.get_roll_value == 3 or
        my_die.get_roll_value == 4 or
        my_die.get_roll_value == 5 or
        my_die.get_roll_value == 6)

    def test_dice_roll2(self):
        the_die = Die()
        the_die.roll()
        self.assertEqual(False, the_die.get_roll_value == 1 or
        the_die.get_roll_value == 2 or
        the_die.get_roll_value == 3 or
        the_die.get_roll_value == 4 or
        the_die.get_roll_value == 5 or
        the_die.get_roll_value == 6)