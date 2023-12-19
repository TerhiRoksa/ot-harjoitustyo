# generoitu koodi alkaa
import sqlite3
import os


class SimpleLoginSystemDB:
    def __init__(self, db_name='users.db', food_db_name='foods.db'):
        self.db_name = db_name
        self.food_db_name = food_db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_user_table()
        self.create_food_table()

    def _get_connection(self, db_name=None):
        if db_name is None:
            db_name = self.db_name
        return sqlite3.connect(db_name)

    def _get_cursor(self, connection):
        return connection.cursor()

    def create_user_table(self):
        with self._get_connection() as connection:
            cursor = self._get_cursor(connection)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                )
            ''')

    def create_food_table(self):
        with self._get_connection(self.food_db_name) as connection:
            cursor = self._get_cursor(connection)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS foods (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    food_name TEXT NOT NULL,
                    calories REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')

    def clear_data(self):
        # Poista kaikki tiedot käyttäjätietokannasta
        with self._get_connection() as connection:
            cursor = self._get_cursor(connection)
            cursor.execute('DELETE FROM users')

        # Poista kaikki tiedot ruokatietokannasta
        with self._get_connection(self.food_db_name) as connection:
            cursor = self._get_cursor(connection)
            cursor.execute('DELETE FROM foods')

        print("Tietokannan tiedot tyhjennetty onnistuneesti.")

    def clear_user_data(self, user_id):
        with self._get_connection(self.food_db_name) as connection:
            cursor = self._get_cursor(connection)
            cursor.execute('DELETE FROM foods WHERE user_id=?', (user_id,))
        print("Käyttäjän tiedot tyhjennetty onnistuneesti.")

    def drop_food_database(self):
        if os.path.exists(self.food_db_name):
            os.remove(self.food_db_name)
            # generoitu koodi päättyy
            print(f"Database {self.food_db_name} dropped successfully.")
