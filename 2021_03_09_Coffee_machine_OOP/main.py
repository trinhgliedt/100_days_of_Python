from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
status = "on"

while status == "on":
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        status = choice
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        if resource_sufficient:
            payment_accepted = money_machine.make_payment(drink.cost)
            if payment_accepted:
                coffee_maker.make_coffee(drink)

