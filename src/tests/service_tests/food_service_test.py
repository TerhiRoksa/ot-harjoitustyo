import unittest
from services.food_service import FoodService
from repositories.database import SimpleLoginSystemDB


class TestFoodService(unittest.TestCase):

    def setUp(self):
        self.login_system = SimpleLoginSystemDB()
        self.login_system.clear_data()
        self.food_service = FoodService(self.login_system)

    def test_add_food(self):
        food_name = "tilli"
        calories = 20
        self.food_service.add_food(1, food_name, calories)
        expected_message = f"Ruoka {food_name} lisätty onnistuneesti."
        self.assertEqual("Ruoka tilli lisätty onnistuneesti.",
                         expected_message)

    def test_get_user_foods(self):
        user_id = 1
        food_name = "mansikka"
        calories = 10.0
        self.food_service.add_food(user_id, food_name, calories)
        result = self.food_service.get_user_foods(user_id)
        expected_result = f"{food_name} - {calories} kcal"
        self.assertEqual(str(result[0]), expected_result)
