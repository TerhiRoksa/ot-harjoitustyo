# generoitu koodi alkaa
import tkinter as tk
from database import SimpleLoginSystemDB
from repositories.calorie_counter import CalorieCounter
from repositories.food import Food
from ui.scrolledframe import ScrolledFrame


class View(tk.Frame):
    def __init__(self, master, login_system, calorie_counter, username, on_logout):
        super().__init__(master)
        self.master = master
        master.geometry("500x800")
        master.title("Painonhallintasovellus")
        self.username = username
        self.calorie_counter = calorie_counter
        self.login_system = login_system
        self.scrolled_frame = ScrolledFrame(master)
        self.scrollable_frame = self.scrolled_frame.scrollable_frame
        self.on_logout_external = on_logout

    def create_main_view(self):

        app_name_font = ("Helvetica", 20)
        self.app_name_label = tk.Label(
            self.master, text="Painonhallintasovellus", font=app_name_font)
        self.app_name_label.pack(in_=self.scrollable_frame, pady=20)

        self.saved_label = tk.Label(
            self.master, text="Näytä tallennetut ruokatiedot.")
        self.saved_label.pack(in_=self.scrollable_frame, pady=10)

        self.button = tk.Button(
            self.master, text="Näytä", command=lambda: self.show_foods(self.login_system.get_user(self.username)))
        self.button.pack(in_=self.scrollable_frame, pady=10)

        self.saved_food_list_text = tk.Text(self.master, height=4, width=30)
        self.saved_food_list_text.pack(in_=self.scrollable_frame, pady=10)

        self.label = tk.Label(self.master, text="Lisää syömäsi ruoka")
        self.label.pack(in_=self.scrollable_frame, pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(in_=self.scrollable_frame, pady=10,
                        side="top", anchor="center")

        self.calorie_label = tk.Label(
            self.master, text="kirjoita tähän kalorit:")
        self.calorie_label.pack(in_=self.scrollable_frame, pady=5)

        self.calorie_entry = tk.Entry(self.master)
        self.calorie_entry.pack(in_=self.scrollable_frame, pady=5)

        self.button = tk.Button(
            self.master, text="Lisää ruokatieto", command=self.button_click)
        self.button.pack(in_=self.scrollable_frame, pady=10)

        self.food_list_text = tk.Text(self.master, height=4, width=30)
        self.food_list_text.pack(in_=self.scrollable_frame, pady=10)

        """"
        self.add_button = tk.Button(
            master, text="Laske kaloreita", command=self.add_calories)
        self.add_button.pack(in_=self.scrollable_frame, pady=10)
        """

        self.total_label = tk.Label(
            self.master, text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")
        self.total_label.pack(in_=self.scrollable_frame, pady=10)

        self.clear_data_button = tk.Button(
            self.master, text="Tyhjennä tallennetut ruokatiedot", command=self.clear_user_data)
        self.clear_data_button.pack(in_=self.scrollable_frame, pady=10)

        self.clear_label = tk.Label(self.master, text="")
        self.clear_label.pack(in_=self.scrollable_frame, pady=5)

        self.logout_button = tk.Button(
            self.master, text="Kirjaudu ulos.", command=self.on_logout_external)
        self.logout_button.pack(in_=self.scrollable_frame, pady=10)

        self.scrolled_frame.pack(fill="both", expand=True)

    def button_click(self):
        user_input = self.entry.get()
        calories = self.calorie_entry.get()
        user_id = self.login_system.get_user(self.username)
        self.label.config(text=f"Lisätty ruoka: {user_input}")
        if user_id is not None:
            self.add_food(user_id=user_id, food_name=user_input,
                          calories=calories)
            self.update_food_list(user_id)
        else:
            print("Käyttäjää ei löytynyt.")

        self.entry.delete(0, tk.END)
        self.calorie_entry.delete(0, tk.END)

    def add_food(self, user_id, food_name, calories):
        self.login_system.add_food(
            user_id=user_id, food_name=food_name, calories=calories)
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

    def update_food_list(self, user_id):
        user_foods = self.login_system.get_user_foods(user_id=user_id)
        self.food_list_text.delete(1.0, tk.END)
        for food in user_foods:
            self.food_list_text.insert(
                tk.END, f"{food.food_name} - {food.calories} kcal\n")
        self.update_total_calories(user_id)

    def show_foods(self, user_id):
        user_foods = self.login_system.get_user_foods(user_id=user_id)
        self.saved_food_list_text.delete(1.0, tk.END)

        if user_foods:
            for food in user_foods:
                self.saved_food_list_text.insert(tk.END, str(food) + '\n')
        else:
            self.saved_food_list_text.insert(
                tk.END, "Tallennettuja ruokia ei vielä ole.")

    def update_total_calories(self, user_id):
        total_calories = self.login_system.calculate_total_calories(user_id)
        self.total_label.config(text=f"Kokonaiskalorit: {total_calories:.2f}")

    def clear_user_data(self):
        user_id = self.login_system.get_user(self.username)
        if user_id is not None:
            self.login_system.clear_user_data(user_id)
            self.food_list_text.delete(1.0, tk.END)
            self.saved_food_list_text.delete(1.0, tk.END)
            self.update_total_calories(user_id)
            self.clear_label.config(
                text="Käyttäjän tallennetut ruokatiedot tyhjennetty.")
        else:
            print("Käyttäjää ei löytynyt.")

    def on_logout(self):

        if self.on_logout_external:
            self.on_logout_external()

        self.master.withdraw()
        self.master.destroy()

    def main_view_show(self):
        self.master.deiconify()


# generoitu koodi päättyy
