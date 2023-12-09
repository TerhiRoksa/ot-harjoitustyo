# generoitu koodi alkaa
import sqlite3
import hashlib
from repositories.food import Food


class SimpleLoginSystemDB:
    def __init__(self, db_name='users.db', food_db_name='foods.db'):
        self.db_name = db_name
        self.food_db_name = food_db_name
        self.create_user_table()
        self.create_food_table()

    def create_user_table(self):

        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                )
            ''')

    def create_food_table(self):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS foods (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    food_name TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

    def clear_data(self):
        # Poista kaikki tiedot käyttäjätietokannasta
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM users')

        # Poista kaikki tiedot ruokatietokannasta
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM foods')

        print("Tietokannan tiedot tyhjennetty onnistuneesti.")

    def register_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))

    def login_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM users WHERE username=? AND password_hash=?', (username, password_hash))
            user = cursor.fetchone()
            if user:
                return True
            else:
                return False

    def get_user(self, username, db_name='users.db'):
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT id FROM users WHERE username=?', (username,))
            user_id = cursor.fetchone()
            return user_id[0] if user_id else None

    def add_food(self, user_id, food_name):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO foods (user_id, food_name) VALUES (?, ?)', (user_id, food_name))
            print(f"Ruoka {food_name} lisätty onnistuneesti.")

    def get_user_foods(self, user_id):
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM foods WHERE user_id=?', (user_id,))
            foods_data = cursor.fetchall()
            foods = [Food(food_data[2]) for food_data in foods_data]
            return foods

# generoitu koodi päättyy
