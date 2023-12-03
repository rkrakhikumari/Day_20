class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 500,
            "coffee": 300,
            "milk": 500,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Coffee: {self.resources['coffee']}ml")
        print(f"Milk: {self.resources['milk']}ml")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingridients[item] > self.resources[item]:
                print(f"sorry there is not enough {item}")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
            print(f"Here is your {order.name}☕. Enjoy!!!")
