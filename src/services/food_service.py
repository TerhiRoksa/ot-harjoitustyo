import sqlite3
from operators.food import Food
from repositories.database import SimpleLoginSystemDB


class FoodService:
    def __init__(self, login_system, food_db_name='foods.db'):
        self.login_system = login_system
        self.food_db_name = food_db_name

    # generoitu koodi alkaa

    def add_food(self, user_id, food_name, calories):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO foods (user_id, food_name, calories) VALUES (?, ?, ?)',
                (user_id, food_name, calories))
            print(f"Ruoka {food_name} lisätty onnistuneesti.")

    def get_user_foods(self, user_id):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM foods WHERE user_id=?', (user_id,))
            foods_data = cursor.fetchall()
            foods = [Food(food_data[2], food_data[3])
                     for food_data in foods_data]
            return foods

    def calculate_total_calories(self, user_id):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT SUM(calories) FROM foods WHERE user_id=?', (user_id,))
            total_calories = cursor.fetchone()[0]
            return total_calories if total_calories else 0

    # generoitu koodi päättyy
