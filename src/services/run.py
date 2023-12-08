# import tkinter as tk
from ui.log import Log
from ui.view import View
# from database import SimpleLoginSystemDB


class RunApplication:
    def __init__(self, root, login_system, calorie_counter):
        self.root = root
        self.login_system = login_system
        self.calorie_counter = calorie_counter
        self.login_view = Log(
            self.root, self.login_system, self.on_login_success)

    def on_login_success(self):
        Log.hide_login_view(self)
        main_view = View(self.root, self.login_system, self.calorie_counter)
        View.main_view_show(self)

    """  
    def clear_data_if_hide(self):
        self.login_system.clear_data()
        self.login_view = Log(
            self.root, self.login_system, self.on_login_success)
        
    """
