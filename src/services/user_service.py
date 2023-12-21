import hashlib
import sqlite3


class UserService:
    """Luokka, joka käsittelee käyttäjän tietoja
    """

    def __init__(self, storage_system, db_name='users.db'):
        """Luokan konstruktori, joka luo uuden UserServicen

        Args:
            storage_system : tallentaa tiedot
            db_name : käyttjätietojen tallennuspaikka
        """
        self.storage_system = storage_system
        self.db_name = db_name

    # generoitu koodi alkaa

    def register_user(self, username, password):
        """Rekisteröi uuden käyttäjän

        Args:
            username : käyttäjänimi
            password : salasana
        """
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, password_hash))

    def login_user(self, username, password):
        """Kirjaa käyttäjän sisälle sovellukseen

        Args:
            username : käyttäjänimi
            password : salasana

        Returns:
            Totuusarvo, joka kertoo onko käyttäjä jo olemassa
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
        """Hakee käyttäjän

        Args:
            username : käyttäjänimi
            db_name : käyttäjätietojen tallennuspaikka

        Returns:
            Numeron, joka on käyttäjän id-numero tietokannassa.
        """
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT id FROM users WHERE username=?', (username,))
            user_id = cursor.fetchone()
            return user_id[0] if user_id else None

    # generoitu koodi päättyy
