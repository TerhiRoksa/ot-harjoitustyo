# generoitu koodi alkaa
import sqlite3
import hashlib


class SimpleLoginSystemDB:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                )
            ''')

    def register_user(self, username, password):
        # Rekisteröi uusi käyttäjä
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
            print(f"Käyttäjä {username} rekisteröity onnistuneesti.")

    def login_user(self, username, password):
        # Kirjaudu käyttäjä sisään
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM users WHERE username=? AND password_hash=?', (username, password_hash))
            user = cursor.fetchone()
            if user:
                print(f"Kirjautuminen onnistui. Tervetuloa, {username}!")
            else:
                print("Virheellinen käyttäjänimi tai salasana.")
# generoitu koodi päättyy
