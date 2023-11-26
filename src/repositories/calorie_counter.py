# generoitu koodi alkaa
# harjoituksen vuoksi ja omilla muutoksilla

class CalorieCounter:
    def __init__(self):
        self.total_calories = 0

    def add_calories(self, amount):
        self.total_calories += amount

    def get_total_calories(self):
        return self.total_calories

# if __name__ == "__main__":
#   root = tk.Tk()
#   calorie_counter = CalorieCounter()
#   app = CalorieCounterUI(root, calorie_counter)
#   root.mainloop()

# generoitu koodi päättyy
