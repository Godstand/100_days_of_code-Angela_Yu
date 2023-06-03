from data import (MENU, resources, profit)


# create a function to check if there are enough resources to make drink
def is_resource_sufficient(order_ingredient):
    """returns False if there are no resources to make drink"""
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True


def process_coins():
    """please insert coins"""
    # all coins inserted will be converted to dollars
    total_in_dollars = int(input("how many quarters?")) * 0.25
    total_in_dollars += int(input("how many dime?")) * 0.1
    total_in_dollars += int(input("how many nickles?")) * 0.01
    total_in_dollars += int(input("how many pennies?")) * 0.05
    return total_in_dollars


def is_transaction_successful(money_received, drink_cost):
    """check that the user has inserted enough money to purchase the drink they selected"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} dollars in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")


def make_coffee(drink_name, order_ingredient):
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f"Here is your {drink_name}😃. Enjoy!")


is_on = True
while is_on:
    choice = input("WHat would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
