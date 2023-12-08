# generoitu koodi alkaa
import tkinter as tk
from database import SimpleLoginSystemDB
from repositories.calorie_counter import CalorieCounter
from repositories.food import Food


class View:
    def __init__(self, master, login_system, calorie_counter):
        self.master = master
        master.geometry("500x800")
        master.title("Painonhallintasovellus")

        self.calorie_counter = calorie_counter
        self.login_system = login_system

        # app_name_font = ("Helvetica", 20)
        # self.app_name_label = tk.Label(
        #    master, text="Painonhallintasovellus", font=app_name_font)
        # self.app_name_label.pack(pady=20)

        self.label = tk.Label(master, text="Lisää syömäsi ruoka")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.button = tk.Button(
            master, text="Lisää ruoka", command=self.button_click)
        self.button.pack(pady=10)

        self.food_list_text = tk.Text(master, height=4, width=30)
        self.food_list_text.pack(pady=10)

        self.calorie_label = tk.Label(master, text="kirjoita tähän kalorit:")
        self.calorie_label.pack(pady=5)

        self.calorie_entry = tk.Entry(master)
        self.calorie_entry.pack(pady=5)

        self.add_button = tk.Button(
            master, text="Lisää kalorit", command=self.add_calories)
        self.add_button.pack(pady=10)

        self.total_label = tk.Label(
            master, text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")
        self.total_label.pack(pady=10)

    def button_click(self):
        user_input = self.entry.get()
        self.label.config(text=f"Lisätty ruoka: {user_input}")
        self.add_food()

    def add_food(self):
        food_name = self.entry.get()
        self.login_system.add_food(user_id=1, food_name=food_name)
        self.update_food_list()

    def add_calories(self):
        try:
            entered_calories = float(self.calorie_entry.get())
            self.calorie_counter.add_calories(entered_calories)
            self.total_label.config(
                text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")
        except ValueError:
            self.total_label.config(
                text="Virheellinen syöte. Anna kelvollinen luku.")

    def update_content(self, calorie_counter):
        self.calorie_counter = calorie_counter
        self.total_label.config(
            text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")

    def update_food_list(self):
        user_foods = self.login_system.get_user_foods(user_id=1)
        self.food_list_text.delete(1.0, tk.END)
        for food in user_foods:
            self.food_list_text.insert(tk.END, str(food) + '\n')
        # print("Käyttäjän ruoat:", user_foods)

    def main_view_show(self):
        self.root.deiconify()

# generoitu koodi päättyy
