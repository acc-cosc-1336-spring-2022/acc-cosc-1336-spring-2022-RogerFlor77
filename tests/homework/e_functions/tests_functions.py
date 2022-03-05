import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds
from src.homework.e_functions.value_return import time_from_utc


class Test_Config(unittest.TestCase):
    def get_hour(self):
        self.assertEqual(1, get_hour(3600))
        self.assertEqual(1, get_hour(3600))

    def get_minutes(self):
        self.assertEqual(3, get_minutes(3800))
        self.assertEqual(0, get_minutes(3600))

    def get_seconds(self):
        self.assertEqual(20, get_seconds(3800))
        self.assertEqual(0, get_seconds(3600))

    def time_from_utc(self):
        self.assertEqual(15, time_from_utc(-5, 20))

    def time_from_utc(self):
        self.assertEqual(14, time_from_utc(-6, 20))

    def time_from_utc(self):
        self.assertEqual(13, time_from_utc(-7, 20))

    def time_from_utc(self):
        self.assertEqual(12, time_from_utc(-8, 20))

