import tkinter as tk
#from ui.view import View
from repositories.calorie_counter import CalorieCounter
#from ui.log import Log
from database import SimpleLoginSystemDB
from services.run_application import RunApplication


def main():
    root = tk.Tk()
    calorie_counter = CalorieCounter()
    login_system = SimpleLoginSystemDB()
    #login_system.clear_data()
   # main_view = View(root, login_system, calorie_counter)
    
    #login_view = Log(root, login_system, main_view.show)
    #login_view = Log(root, login_system, on_login_success)
    #login_view.show()
    app = RunApplication(root, login_system, calorie_counter)
    root.mainloop()
    

#def on_login_success():
    # Tämä funktio kutsutaan, kun kirjautuminen onnistuu
    # Piilota kirjautumisnäkymä
    #login_view.hide()
    
    # Luo pääsovelluksen näkymä
   # main_root = tk.Toplevel()
   # main_view = View(main_root, login_system, calorie_counter)
    
    
    #root.mainloop()


if __name__ == "__main__":
    main()
