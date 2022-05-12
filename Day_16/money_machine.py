"""
    This program implements the money processing class of the
    Coffee Machine
"""


class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self._profit = 0
        self._money_received = 0

    # Defining Getters and Setter
    def get_profit(self):
        return self._profit

    def get_money_received(self):
        return self._money_received

    def report(self):
        print(f"Money: {self.CURRENCY}{self._profit}")

    def process_coins(self):
        """Returns a total calculated from coins inserted"""
        print("Please insert coins")
        for coin in self.COIN_VALUES:
            self._money_received += int(input(f"How many {coin}? ")) * self.COIN_VALUES[coin]
        return self._money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient"""
        paid_amount = self.process_coins()

        if paid_amount >= cost:
            change = round(paid_amount - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change")
            self._profit += cost
            self._money_received = 0
            return True

        else:
            print("Sorry that's not enough money. Money refunded!")
            self._money_received = 0
            return False