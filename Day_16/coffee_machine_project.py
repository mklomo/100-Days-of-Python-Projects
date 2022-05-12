"""
Building a Coffee Machine is OOP
"""

from menu import MenuItem, Menu

from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()

coffee_menu = Menu()

coffee_payment = MoneyMachine()


# Same Session flag
same_session = True

while same_session:

    # Now select from the coffee_menu
    coffee_menu.get_items()

    # Find the drink you want from the options

    coffee_choice = input(f"What would you like? {coffee_menu.get_items()}: \n").lower()

    if coffee_choice == "off":
        same_session = False

    elif coffee_choice == "report":
        # TODO: 1 : Print Report
        coffee_machine.report()
        coffee_payment.report()

    else:
        avail_option = coffee_menu.find_drink(order_name=coffee_choice)

        if avail_option in coffee_menu.get_menu():
            # TODO: 2 : Check Resources Sufficient
            if coffee_machine.is_resource_sufficient(avail_option):
                # TODO: 3 : Process Coins
                # TODO: 4 : Check Transaction
                payment_success = coffee_payment.make_payment(avail_option.get_cost())

                # TODO : 5 : Make Coffee
                if payment_success:
                    coffee_machine.make_coffee(avail_option)

                else:
                    same_session = False

            else:
                print("Insufficient Resources")
                same_session = False
