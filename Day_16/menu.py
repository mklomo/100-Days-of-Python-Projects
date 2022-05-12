"""
    This program defines the MenuItem class
"""


class MenuItem:
    """ Models each menu"""

    def __init__(self, name, water, milk, coffee, cost):
        self._name = name
        self._cost = cost
        self._ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

    # Define the getters and setters

    def get_name(self):
        """This method gets the name of the MenuItem"""
        return self._name

    def get_cost(self):
        """This method gets the cost of the MenuItem"""
        return self._cost

    def get_ingredients(self):
        """This method returns the ingredients of the MenuItem"""
        return self._ingredients

    def set_name(self, name):
        """This method sets the name of the MenuItem"""
        self._name = name
        return self._name

    def set_cost(self, cost):
        """This method sets the cost of the MenuItem"""
        self._cost = cost
        return self._cost

    def set_ingredients(self, ingredients):
        """This method sets the ingredients of the MenuItem"""
        self._ingredients = ingredients
        return self._ingredients

    # Defining a Menu class


class Menu:
    def __init__(self):
        self._menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),

            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),

            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    # Define a getter

    def get_menu(self):
        """Returns the menu"""
        return self._menu

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.get_menu():
            options += f"{item.get_name()} / "
        return options

    def set_menu(self, menu):
        self._menu = menu
        return self._menu

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists,
        otherwise, returns none
        """
        for item in self._menu:
            if item._name == order_name:
                return item
        print("Sorry, not available!")
