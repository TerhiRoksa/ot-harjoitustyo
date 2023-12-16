import unittest
from services.calorie_counter import CalorieCounter


class TestCalorieCounter(unittest.TestCase):

    def setUp(self):
        self.counter = CalorieCounter()

    def test_add_calories(self):
        self.counter.add_calories(250)
        self.assertEqual(self.counter.get_total_calories(), 250)

    def test_total_calories(self):
        self.counter.add_calories(30)
        self.counter.add_calories(50)
        self.assertEqual(self.counter.get_total_calories(), 80)
