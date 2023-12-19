import tkinter as tk
from services.calorie_counter import CalorieCounter
from ui.run import RunApplication
from repositories.database import StorageSystemDB


def main():
    root = tk.Tk()
    calorie_counter = CalorieCounter()
    storage_system = StorageSystemDB()

    # storage_system.clear_data()
    # storage_system.drop_food_database()

    RunApplication(root, storage_system, calorie_counter)

    root.mainloop()


if __name__ == "__main__":
    main()
