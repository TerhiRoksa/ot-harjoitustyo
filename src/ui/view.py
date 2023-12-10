# generoitu koodi alkaa
import tkinter as tk
from database import SimpleLoginSystemDB
from repositories.calorie_counter import CalorieCounter
from repositories.food import Food
from services.scrolledframe import ScrolledFrame


class View:
    def __init__(self, master, login_system, calorie_counter, username):
        self.master = master
        master.geometry("500x800")
        master.title("Painonhallintasovellus")
        self.username = username
        self.calorie_counter = calorie_counter
        self.login_system = login_system
        self.scrolled_frame = ScrolledFrame(master)
        self.scrollable_frame = self.scrolled_frame.scrollable_frame

        # self.empty_space = tk.Label(self.scrollable_frame, text="", width=15)
        # self.empty_space.pack(side="left", fill="both")
        self.empty_space_top = tk.Label(
            self.scrollable_frame, text="", height=5)
        self.empty_space_top.pack(side="top", fill="both")

        app_name_font = ("Helvetica", 20)
        self.app_name_label = tk.Label(
            master, text="Painonhallintasovellus", font=app_name_font)
        self.app_name_label.pack(in_=self.scrollable_frame, pady=20)

        self.saved_label = tk.Label(master, text="Näytä tallennetut ruokatiedot.")
        self.saved_label.pack(in_=self.scrollable_frame, pady=10)

        self.button = tk.Button(
            master, text="Näytä", command=lambda: self.show_foods(self.login_system.get_user(self.username)))
        self.button.pack(in_=self.scrollable_frame, pady=10)

        self.saved_food_list_text = tk.Text(master, height=4, width=30)
        self.saved_food_list_text.pack(in_=self.scrollable_frame, pady=10)

        self.label = tk.Label(master, text="Lisää syömäsi ruoka")
        self.label.pack(in_=self.scrollable_frame, pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(in_=self.scrollable_frame, pady=10,
                        side="top", anchor="center")

        self.button = tk.Button(
            master, text="Lisää ruoka", command=self.button_click)
        self.button.pack(in_=self.scrollable_frame, pady=10)

        self.food_list_text = tk.Text(master, height=4, width=30)
        self.food_list_text.pack(in_=self.scrollable_frame, pady=10)

        self.calorie_label = tk.Label(master, text="kirjoita tähän kalorit:")
        self.calorie_label.pack(in_=self.scrollable_frame, pady=5)

        self.calorie_entry = tk.Entry(master)
        self.calorie_entry.pack(in_=self.scrollable_frame, pady=5)

        self.add_button = tk.Button(
            master, text="Lisää kalorit", command=self.add_calories)
        self.add_button.pack(in_=self.scrollable_frame, pady=10)

        self.total_label = tk.Label(
            master, text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")
        self.total_label.pack(in_=self.scrollable_frame, pady=10)

        self.logout_button = tk.Button(
            master, text="Kirjaudu ulos. Poistu sovelluksesta.", command=self.logout)
        self.logout_button.pack(in_=self.scrollable_frame, pady=10)

        self.scrolled_frame.pack(fill="both", expand=True)

    def button_click(self):
        user_input = self.entry.get()
        calories = self.calorie_entry.get()
        user_id = self.login_system.get_user(self.username)
        self.label.config(text=f"Lisätty ruoka: {user_input}")
        if user_id is not None:
            self.add_food(user_id=user_id, food_name=user_input, calories=calories)
            self.update_food_list(user_id)
        else:
            print("Käyttäjää ei löytynyt.")
        """"
        if user_id is not None:
            self.add_food(user_id=user_id)
        else:
            print("Käyttäjää ei löytynyt.")
        

    def add_food(self, user_id):
        food_name = self.entry.get()
        self.login_system.add_food(user_id=user_id, food_name=food_name)
        self.update_food_list(user_id)
    """
        
    def add_food(self, user_id, food_name, calories):
        self.login_system.add_food(user_id=user_id, food_name=food_name, calories=calories)
        self.update_food_list(user_id)
    
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
    """"
    def update_food_list(self, user_id):
        user_foods = self.login_system.get_user_foods(user_id=user_id)
        self.food_list_text.delete(1.0, tk.END)
        for food in user_foods:
            self.food_list_text.insert(tk.END, str(food) + '\n')
        # print("Käyttäjän ruoat:", user_foods)
    """

    def update_food_list(self, user_id):
        user_foods = self.login_system.get_user_foods(user_id=user_id)
        self.food_list_text.delete(1.0, tk.END)
        for food in user_foods:
            self.food_list_text.insert(tk.END, f"{food.name} - {food.calories} kcal\n")

    def show_foods(self, user_id):
        user_foods = self.login_system.get_user_foods(user_id=user_id)
        self.saved_food_list_text.delete(1.0, tk.END)  # Clear the existing content

        if user_foods:
            for food in user_foods:
                self.saved_food_list_text.insert(tk.END, str(food) + '\n')
        else:
            self.saved_food_list_text.insert(tk.END, "Tallennettuja ruokia ei vielä ole.")


    def logout(self):
        # toistaiseksi sovelluksesta poistuminen, 
        # koska näyttöjen näkymien kanssa on ongelma.
        self.master.destroy()

    def main_view_show(self):
        self.master.deiconify()


# generoitu koodi päättyy
