
from database import SimpleLoginSystemDB
from ui.view import View
import tkinter as tk

class Log:
    def __init__(self):
        self.login_system = SimpleLoginSystemDB()
        self.handle_login()

    def handle_login(self):
        print("handle_login -metodi käynnistyy")

        while True:
            print("\nValitse toiminto:")
            print("1. Rekisteröi uusi käyttäjä")
            print("2. Kirjaudu sisään")
            print("3. Poistu")

            choice = input("Valinta: ")

            if choice == "1":
                username = input("Syötä käyttäjänimi: ")
                password = input("Syötä salasana: ")
                self.login_system.register_user(username, password)

            elif choice == "2":
                username = input("Syötä käyttäjänimi: ")
                password = input("Syötä salasana: ")
                if self.login_system.login_user(username, password):
                    self.open_main_window()
                    break

            elif choice == "3":
                #open_main_window(self)
                print("Poistutaan.")
                break

            else:
                print("Virheellinen valinta. Yritä uudelleen.")

        print("handle_login -metodi päättyy")

    def open_main_window(self):
        # Luo uusi ikkuna
        main_window = tk.Toplevel()
        
        # Avaa pääsovelluksen näkymä
        view = View(main_window)

