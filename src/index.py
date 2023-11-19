import tkinter as tk
from ui.view import View
from repositories.calorie_counter import CalorieCounter

def main():
    root = tk.Tk()
    calorie_counter = CalorieCounter()
    app = View(root, calorie_counter)
    root.mainloop() 


if __name__ == "__main__":
    main()
