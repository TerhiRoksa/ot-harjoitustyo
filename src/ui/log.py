import tkinter as tk
from repositories.database import StorageSystemDB
from services.user_service import UserService

# generoitu koodi alkaa


class Log:
    """Luokka, joka vastaa kirjautumisnäytöstä
    """

    def __init__(self, root, storage_system, on_login_success):
        """Luokan konstruktori, joka luo uuden Log:in

        Args:
            root : pääikkuna
            storage_system : tallentaa tiedot
            on_login_success : vastaa onnistuneen kirjautumisen jälkeisestä toiminnasta
        """
        self.root = root
        self.storage_system = storage_system
        self.user_service = UserService(storage_system)
        self.on_login_success = on_login_success
        self.create_login_view()
        root.title("Kirjautuminen")

    def create_login_view(self):
        """Vastaa kirjautumistoiminnoista
        """
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
        """Vastaa uuden käyttäjä rekisteröitymistoiminnoista
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.reg_label.config(
                text="Käyttäjänimi ja salasana eivät voi olla tyhjiä.")
            return

        self.user_service.register_user(username, password)
        self.reg_label.config(
            text=f"Käyttäjä {username} rekisteröity onnistuneesti.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def login(self):
        """Käyttäjän kirjautuminen
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        login_successful = self.user_service.login_user(username, password)

        if login_successful:
            print("Kirjautuminen onnistui.")

            self.on_login_success()

        else:
            self.log_label.config(
                text="Virheellinen käyttäjänimi tai salasana.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# generoitu koodi päättyy

    def hide_login_view(self):
        """piilottaa kirjautumisnäkymän
        """
        self.root.withdraw()

    def show_login_view(self):
        """näyttää kirjautumisnäkymän
        """
        self.root.deiconify()
