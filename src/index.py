import tkinter as tk
from ui.view import View
from repositories.calorie_counter import CalorieCounter
from ui.log import Log
from database import SimpleLoginSystemDB


def main():
    root = tk.Tk()
    calorie_counter = CalorieCounter()
    login_system = SimpleLoginSystemDB()

    login_view = Log(root, login_system)
    main_view = View(root, login_system, calorie_counter)

    root.mainloop()


if __name__ == "__main__":
    main()
