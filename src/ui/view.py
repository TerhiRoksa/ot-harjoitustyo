# generoitu koodi alkaa
# omilla muutoksilla
import tkinter as tk
from tkinter import messagebox
from database import SimpleLoginSystemDB
from repositories.calorie_counter import CalorieCounter
# from ui.login import Log


class View:
    def __init__(self, master, login_system, calorie_counter):
        self.master = master
        master.geometry("500x800")
        self.empty_space_frame = tk.Frame(master, height=40)
        self.empty_space_frame.pack()
        master.title("Painonhallintasovellus")
        self.calorie_counter = calorie_counter
        self.login_system = login_system

        app_name_font = ("Helvetica", 20)
        self.app_name_label = tk.Label(
            master, text="Painonhallintasovellus", font=app_name_font)
        self.app_name_label.pack(pady=20)

        self.label = tk.Label(master, text="Lisää syömäsi ruoka")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.button = tk.Button(
            master, text="Lisää ruoka", command=self.button_click)
        self.button.pack(pady=20)

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

    def add_calories(self):
        try:
            entered_calories = float(self.calorie_entry.get())
            self.calorie_counter.add_calories(entered_calories)
            self.total_label.config(
                text=f"Kokonaiskalorit: {self.calorie_counter.get_total_calories():.2f}")
        except ValueError:
            self.total_label.config(
                text="Virheellinen syöte. Anna kelvollinen luku.")

# generoitu koodi päättyy
