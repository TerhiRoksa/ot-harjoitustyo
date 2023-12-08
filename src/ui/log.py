import tkinter as tk
from database import SimpleLoginSystemDB
# from ui.view import View
# generoitu koodi alkaa


class Log:
    def __init__(self, root, login_system, on_login_success):
        self.root = root
        self.login_system = login_system
        self.on_login_success = on_login_success
        self.create_login_ui()
        root.title("Kirjautuminen")

    def create_login_ui(self):
        tk.Label(self.root, text="Syötä käyttäjänimi:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        tk.Label(self.root, text="Syötä salasana:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        self.log_label = tk.Label(text="Kirjaudu tästä.")
        self.log_label.pack(pady=5)
        tk.Button(self.root, text="Kirjaudu", command=self.login).pack()

        self.reg_label = tk.Label(
            text="Luo tästä uusi käyttäjätunnus ja salasana.")
        self.reg_label.pack(pady=5)
        tk.Button(self.root, text="Rekisteröi uusi käyttäjä",
                  command=self.register).pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.login_system.register_user(username, password)
        self.reg_label.config(
            text=f"Käyttäjä {username} rekisteröity onnistuneesti.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        login_successful = self.login_system.login_user(username, password)

        if login_successful:
            self.log_label.config(
                text=f"Kirjautuminen onnistui. Tervetuloa, {username}!")
            # self.hide_login_view()
            self.on_login_success()

        else:
            self.log_label.config(
                text="Virheellinen käyttäjänimi tai salasana.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def hide_login_view(self):
        # Piilota kirjautumisnäkymä
        self.root.withdraw()

# generoitu koodi päättyy
