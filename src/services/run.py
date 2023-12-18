import tkinter as tk
from ui.log import Log
from ui.view import View


class RunApplication:
    def __init__(self, master, login_system, calorie_counter):
        self.root = master
        self.login_system = login_system
        self.calorie_counter = calorie_counter
        self.login_view = Log(
            self.root, self.login_system, self.on_login_success)
        self.login_view.show_login_view()

    def on_login_success(self):

        self.username = self.login_view.username_entry.get()
        self.main_view = tk.Toplevel(self.root)
        view = View(self.main_view, self.login_system,
                    self.calorie_counter, self.username, self.on_logout)
        view.create_main_view()
        self.login_view.hide_login_view()
        return True

    def on_logout(self):

        self.login_view.show_login_view()
        self.main_view.withdraw()
