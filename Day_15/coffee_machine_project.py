"""
    This program simulates a virtual coffee machine 
"""


# Coffee Flavors
## -> Expresso : 50ml of Water, 18g of coffee
## -> Latte : 200ml of water, 24g of coffee, 150ml of milk
## -> Capuccino : 250ml of water, 24g of coffee, and 100ml of milk


# Price
# Espresso : $1.50
# Latte : $2.50
# Capuccino : $3.00


# Starting Ingredients in Coffee Machine's Tank
# 300ml of water
# 200ml of milk
# 100ml of coffee


# Global Variable
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#  Program Requirements
# TODO 1 : Prompt User
def prompt():
    """
    This function prompts the user for an input i.r. espresso, latte, cappuccino

    input: str

    output: user_choice (str)
    """
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    return user_choice




# TODO 2 - Check if resources are efficient when the user orders a drink
def check_resources(coffee_choice: str, water_level: int, milk_level: int, coffee_level: int):
    """
    This function checks whether the current resources are sufficient for the order

    input: water, milk and coffee (int) required

    output: boolean

    """
    global MENU
    
    # Select the Coffee Option
    coffee_selected = MENU[coffee_choice]["ingredients"]

    # Now check the ingredients
    water_reqd = coffee_selected["water"]
    milk_reqd = coffee_selected["milk"]
    coffee_reqd = coffee_selected["coffee"]

    if (
        (water_level >= water_reqd)
        and (milk_level >= milk_reqd)
        and (coffee_level >= coffee_reqd)
    ):
        return True
    
    else:
        return False

        
        
# TODO 3 - Process Coins
def payment_request():
    
    # The coffee machine is coin operated hence accepts the ff coins
    # Penny:    1 cent      :   $0.01
    # Dime:     10 cents    :   $0.10
    # Nickel:   5 cents     :   $0.05
    # Quarter:  25 cents    :   0.25
    
    quarter = int(input("\nHow many quarters? "))
    dime = int(input("\nHow many dimes? "))
    nickel = int(input("\nHow many nickels? "))
    penny = int(input("\nHow many pennies? "))

    total_payment = (
        (quarter * (0.25)) + (dime * (0.1)) + (nickel * (0.05)) + (penny * (0.01))
    )
    
    return total_payment




def process_coins(coffee_choice, payment_amount):
    """
    This function processes coins

    input: coffee choice (str) and coins (float)

    output: amount (int)

    """

    global MENU



    coffee_cost = MENU[coffee_choice]["cost"]

    # Calculate Change
    change = payment_amount - coffee_cost
    return change



# TODO: 4
def make_coffee(coffee_choice: str, water_level: int, milk_level: int, coffee_level: int):
 
    global MENU
    
    # The Coffee Option
    coffee_selected = MENU[coffee_choice]["ingredients"]

    # Now check the ingredients
    water_reqd = coffee_selected["water"]
    milk_reqd = coffee_selected["milk"]
    coffee_reqd = coffee_selected["coffee"]

    water_level -= water_reqd
    milk_level -= milk_reqd
    coffee_level -= coffee_reqd

    return water_level, milk_level, coffee_level





if __name__ == '__main__':
    print("\n")

    # Welcome Statement
    print("Welcome to Marvin's Coffee Machine\n")


    # Same session
    same_session = True

    # Lets check resources
    res_water_level = resources["water"]
    res_milk_level = resources["milk"]
    res_coffee_level = resources["coffee"]

    payment_amount = 0
    
    change = 0

    # Lets prompt the user
    selected_option = prompt()    

    while same_session:
        
        # Depending on the prompt, lets  do the ff
        coffee_options = ["cappuccino", "latte", "espresso"]

        if selected_option in coffee_options:
            # Lets make the required coffee
            make_coffee_flag = check_resources( 
                coffee_choice = selected_option,
                water_level  = res_water_level,
                coffee_level = res_coffee_level,
                milk_level = res_milk_level
            )

            # if sufficient resources exist, process the coins
            if make_coffee_flag:
                
                # Ask user for payment at the first instance
                if change == 0:
                    paid_amount = payment_request()
                
                else: 
                    # Set the change
                    paid_amount = change
                
                # Get the Change
                change = process_coins(coffee_choice = selected_option, payment_amount = paid_amount)

                # Now lets continue to make the coffee
                if change >= 0:
                    # Reset the reservoir levels
                    (res_water_level, res_milk_level, res_coffee_level) = make_coffee(
                        coffee_choice = selected_option,
                        water_level = res_water_level,
                        milk_level = res_milk_level,
                        coffee_level =  res_coffee_level
                    )
    
                    # Print out the new Coffee
                    if change > 0:
                        
                        print(
                            f"\nHere is your {selected_option=} ☕️ and your change {round(change,2)}. Please Enjoy!\n"
                        )
                        
                        # Ask the user for another option
                        selected_option = prompt()

                    else:
                        
                        print(f"\nHere is your {selected_option=}. Please Enjoy\n")
                        
                        
                        
                else:
                    
                    print("Insufficient deposit 💰!")
                    
                    break

            else:
                
                print("Insufficient Resources! Please refill the resource tank 🥴")
                
                print(
                    f"\nHere is your change {round(change,2)}. Please Enjoy!\n"
                    )
                
                break

        elif selected_option == "off":
            
            print("\nHave a coffee-filled day!😎")
            
            same_session = False
            
            break

        elif selected_option == "report":
            print(f"The current water level is: {res_water_level}")
            print(f"The current milk level is: {res_milk_level}")
            print(f"The current coffee level is: {res_coffee_level}")
            print(f"The current cash balance is: {change}")

            # Print prompt
            selected_option = prompt()

            # Lets continue
            same_session = True
