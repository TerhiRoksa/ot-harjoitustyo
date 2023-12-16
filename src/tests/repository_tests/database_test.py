import unittest
from repositories.database import SimpleLoginSystemDB


class TestSimpleLoginSystemDB(unittest.TestCase):

    def setUp(self):
        self.database = SimpleLoginSystemDB()

    def test_add_food(self):
        food_name = "tilli"
        self.database.add_food(1, food_name)
        expected_message = f"Ruoka {food_name} lisätty onnistuneesti."
        self.assertEqual("Ruoka tilli lisätty onnistuneesti.",
                         expected_message)
