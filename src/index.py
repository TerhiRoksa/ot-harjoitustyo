import tkinter as tk
from services.calorie_counter import CalorieCounter
from repositories.database import SimpleLoginSystemDB
from services.run import RunApplication


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
