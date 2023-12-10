
from ui.log import Log
from ui.view import View


class RunApplication:
    def __init__(self, master, login_system, calorie_counter):
        self.root = master
        self.login_system = login_system
        self.calorie_counter = calorie_counter
        self.login_view = Log(
            self.root, self.login_system, self.on_login_success)

    def on_login_success(self):
        username = self.login_view.username_entry.get()
        self.login_view.hide_login_view()
        main_view = View(self.root, self.login_system,
                         self.calorie_counter, username)
        main_view.main_view_show()
        

    """  
    def clear_data_if_hide(self):
        self.login_system.clear_data()
        self.login_view = Log(
            self.root, self.login_system, self.on_login_success)
    """
