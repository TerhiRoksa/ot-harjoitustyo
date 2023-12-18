import unittest
import tkinter as tk
from services.run import RunApplication
from repositories.database import SimpleLoginSystemDB
from services.calorie_counter import CalorieCounter


class TestRun(unittest.TestCase):

    def setUp(self):
        self.master = tk.Tk()
        self.login_system = SimpleLoginSystemDB()
        self.calorie_counter = CalorieCounter()
        self.run = RunApplication(
            self.master, self.login_system, self.calorie_counter)

    def test_run(self):
        result = self.run.on_login_success()
        self.assertTrue(result, "Sovelluksen näyttäminen epäonnistui.")
