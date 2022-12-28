from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# INIT VARIABLES
is_continue = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_continue:

    order = input(f"What would you like?({menu.get_items()}):").lower()
    if order == "off":
        print("Coffee machine is now turning off....")
        is_continue = False
    elif order == "report":
        #   Show current resource values
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



