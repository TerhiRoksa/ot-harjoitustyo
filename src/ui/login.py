
from database import SimpleLoginSystemDB
from ui.view import View
import tkinter as tk


class Log:
    def __init__(self):
        pass
        #self.login_system = SimpleLoginSystemDB()
        #self.handle_login()

    def handle_login(self, login_system):
        #print("handle_login -metodi käynnistyy")
        # generoitu koodi alkaa
        while True:
            print("\nValitse toiminto:")
            print("1. Rekisteröi uusi käyttäjä")
            print("2. Kirjaudu sisään")
            print("3. Poistu/Sovellukseen")

            choice = input("Valinta: ")

            if choice == "1":
                username = input("Syötä käyttäjänimi: ")
                password = input("Syötä salasana: ")
                login_system.register_user(username, password)

            elif choice == "2":
                username = input("Syötä käyttäjänimi: ")
                password = input("Syötä salasana: ")
                if login_system.login_user(username, password):
                    self.open_main_window()
                    break

            elif choice == "3":
                #open_main_window(self)
                print("Poistutaan kirjautumisesta.")
                break

            else:
                print("Virheellinen valinta. Yritä uudelleen.")

        #print("handle_login -metodi päättyy")

    def open_main_window(self):

        main_window = tk.Toplevel()
        view = View(main_window)
        # generoitu koodi päättyy

