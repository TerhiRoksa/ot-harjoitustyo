import tkinter as tk

class View:
    def __init__(self, master):
        self.master = master
        master.title("Painonhallintasovellus")

        self.label = tk.Label(master, text="Lisää ruoka")
        self.label.pack(pady=40)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=40)
        
        self.button = tk.Button(master, text="Lisää", command=self.button_click)
        self.button.pack(pady=40)

    def button_click(self):
        user_input = self.entry.get()
        self.label.config(text=f"Lisätty ruoka: {user_input}")


