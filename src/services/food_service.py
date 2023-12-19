import sqlite3
from operators.food import Food


class FoodService:
    """Luokka, joka käsittelee käyttäjän syöttämiä ruokatietoja.
    """

    def __init__(self, storage_system, food_db_name='foods.db'):
        """Luokan konstruktori, joka luo uuden FoodServicen.

        Args:
            storage_system : tallentaa tiedot
            food_db_name : ruokatietojen tallennuspaikka
        """
        self.storage_system = storage_system
        self.food_db_name = food_db_name

    # generoitu koodi alkaa

    def add_food(self, user_id, food_name, calories):
        """Lisää ruoan ja sen kalorit käyttäjän ruokatietoihin.

        Args:
            user_id: käyttäjän id-numero tietokannassa
            food_name: ruoka
            calories: kalorit
        """
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO foods (user_id, food_name, calories) VALUES (?, ?, ?)',
                (user_id, food_name, calories))
            print(f"Ruoka {food_name} lisätty onnistuneesti.")

    def get_user_foods(self, user_id):
        """Hakee käyttäjän ruokatiedot.

        Args:
            user_id: käyttäjän id-numero tietokannassa

        Returns:
            Merkkijono, joka kertoo käyttäjän ruoat ja niiden kalorit
        """
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM foods WHERE user_id=?', (user_id,))
            foods_data = cursor.fetchall()
            foods = [Food(food_data[2], food_data[3])
                     for food_data in foods_data]
            return foods

    def calculate_total_calories(self, user_id):
        """Laskee käyttäjän kokonaiskalorimäärän.

        Args:
            user_id: käyttäjän id-numero tietokannassa

        Returns:
            Numero, joka kertoo käyttäjän kokonaiskalorimäärän.
        """
        with sqlite3.connect(self.food_db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT SUM(calories) FROM foods WHERE user_id=?', (user_id,))
            total_calories = cursor.fetchone()[0]
            return total_calories if total_calories else 0

    # generoitu koodi päättyy
