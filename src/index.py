import tkinter as tk
from repositories.calorie_counter import CalorieCounter
from database import SimpleLoginSystemDB
from services.run import RunApplication
from services.user_service import UserService
from services.food_service import FoodService

def main():
    root = tk.Tk()
    calorie_counter = CalorieCounter()
    login_system = SimpleLoginSystemDB()

    # login_system.clear_data()
    # login_system.drop_food_database()

    RunApplication(root, login_system, calorie_counter)

    root.mainloop()


if __name__ == "__main__":
    main()
