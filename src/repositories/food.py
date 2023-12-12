class Food:
    def __init__(self, food_name, calories):
        self.food_name = food_name
        self.calories = calories

    def __str__(self):
        return f"{self.food_name} - {self.calories} kcal"
