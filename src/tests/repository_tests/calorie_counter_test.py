import unittest

from repositories.calorie_counter  import CalorieCounter

class TestCalorieCounter(unittest.TestCase):

	def setUp(self):
	    self.counter = CalorieCounter()

	def test_add_calories(self):
            self.counter.add_calories(250)
            self.assertEqual(self.counter.get_total_calories(), 250)
