class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee

        }
class Menu:
    def __int__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=250),
            MenuItem(name="espresso", water=50, milk=0, coffee=24, cost=150),
            MenuItem(name="cappuccino", water=200, milk=150, coffee=24, cost=300),
            ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
    print("sory that item is not available")