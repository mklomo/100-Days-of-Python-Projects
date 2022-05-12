class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self._resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources"""
        print(f"Water: {self._resources['water']}ml")
        print(f"Milk: {self._resources['milk']} ml")
        print(f"Coffee: {self._resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Return True when order can be made, False if ingredients are insufficient"""
        can_make = True
        for item in drink._ingredients:
            if drink._ingredients[item] > self._resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources"""
        for item in order._ingredients:
            self._resources[item] -= order._ingredients[item]
        print(f"Here is your {order._name}. Enjoy!")
