# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_menu(menu):
    print("----------------------\nHere is the menu:")
    for drink, price in menu.items():
        print(f"{drink}: ${price}")
    print("----------------------")

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
def ask_user_input():
    request = input("What would you like? (espresso/latte/cappuccino): ")
    return request


# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
def turn_machine_off():
    return "off"


# TODO: 3. Print report
def print_report(resource):
    print(f'Water: {resource["water"]}ml')
    print(f'Milk: {resource["milk"]}ml')
    print(f'Coffee: {resource["coffee"]}g')
    print(f'Money: ${resource["money"]}')
    return


# TODO: 4. Check resources sufficient:
def check_resource_sufficient(request, resource, recipes):
    enough_ingredient = True
    recipe = recipes[request]
    for ingredient, quantity in recipe.items():
        if quantity > resource[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            enough_ingredient = False
    return enough_ingredient


# TODO: 5. Process coins
def process_coins(coins):
    user_payment = 0
    print("Please insert coins.")
    for coin_type, value in coins.items():
        no_of_coins = int(input(f"How many {coin_type}?"))
        coins_in_dollar = no_of_coins*value
        user_payment += coins_in_dollar
    print(f"Received ${'{:.2f}'.format(user_payment)} in total.")
    return user_payment


# TODO: 6. Check transaction successful
def verify_transaction_successful(request, user_payment, menu, resource):
    if user_payment < menu[request]:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        if user_payment > menu[request]:
            change = "{:.2f}".format(user_payment - menu[request])
            print(f"Here is ${change} in change.")
        resource["money"] += menu[request]
        return True


# TODO: 7. Make coffee:
def make_coffee(request, resource, recipes):
    drink_recipe = recipes[request]
    for ingredient, quantity in drink_recipe.items():
        resource[ingredient] -= quantity
    print(f"Here is your {request}. Enjoy!")
    return


def operate_machine():
    status = "on"
    resource = {"water": 2000, "milk": 100, "coffee": 100, "money": 0}
    recipes = {"espresso": {"water": 50, "milk": 10, "coffee": 30},
               "latte": {"water": 40, "milk": 15, "coffee": 25},
               "cappuccino": {"water": 45, "milk": 20, "coffee": 35}}
    menu = {"espresso": 2.5, "latte": 2.5, "cappuccino": 2.8}
    coins = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}

    while status == "on":
        print_menu(menu)
        request = ask_user_input()
        if request == "off":
            status = turn_machine_off()
        elif request == "report":
            print_report(resource)
        elif request in menu:
            is_resource_sufficient = check_resource_sufficient(request, resource, recipes)
            if is_resource_sufficient:
                user_payment = process_coins(coins)
                is_transaction_successful = verify_transaction_successful(request, user_payment, menu, resource)
                if is_transaction_successful: make_coffee(request, resource, recipes)
    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    operate_machine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
