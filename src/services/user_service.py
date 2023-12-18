import hashlib
import sqlite3
#from repositories.database import SimpleLoginSystemDB


class UserService:
    def __init__(self, login_system, db_name='users.db'):
        self.login_system = login_system
        self.db_name = db_name

    # generoitu koodi alkaa

    def register_user(self, username, password):
        """AI is creating summary for register_user

        Args:
            username ([type]): [description]
            password ([type]): [description]
        """
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, password_hash))

    def login_user(self, username, password):
        """AI is creating summary for login_user

        Args:
            username ([type]): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM users WHERE username=? AND password_hash=?',
                (username, password_hash))
            user = cursor.fetchone()
            return bool(user)

    def get_user(self, username, db_name='users.db'):
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT id FROM users WHERE username=?', (username,))
            user_id = cursor.fetchone()
            return user_id[0] if user_id else None

    # generoitu koodi päättyy
