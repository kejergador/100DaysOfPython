# IMPORTS
import random


# FUNCTIONS
def check_resources(user_order):
    """Checks the coffee machine if there are enough resources for the current order."""
    should_continue = True
    if user_order == "espresso":
        if resources["water"] < menu[user_order]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            should_continue = False
        if resources["coffee"] < menu[user_order]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            should_continue = False
    else:
        if resources["water"] < menu[user_order]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            should_continue = False
        if resources["milk"] < menu[user_order]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            should_continue = False
        if resources["coffee"] < menu[user_order]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            should_continue = False
    return should_continue


def still_have_resources(machine_resources):
    """Returns true if resources is not equal to 0"""
    have_resources = None
    for resources_key in machine_resources:
        if resources[resources_key] > 0:
            have_resources = True
    return have_resources


def use_resources(user_order, machine_menu, machine_resources):
    """Deduct the resources needed for the user's order and returns the current resources of the machine after the
    user's order. """
    for menu_ingredients_key in machine_menu[user_order]["ingredients"]:
        # print(menu_ingredients_key)  # REPRESENT KEY water, coffee
        # print(menu[order]["ingredients"][menu_ingredients_key])  # REPRESENT VALUES [50,18]
        for resources_key in machine_resources:
            if resources_key == menu_ingredients_key:
                machine_resources[menu_ingredients_key] -= menu[user_order]["ingredients"][menu_ingredients_key]
    print(f"Here is your {user_order} ☕. Enjoy! Come again :)")


def process_coins(user_order, machine_menu):
    """Prompt the user to insert coins."""
    quarter = 0.25
    dimes = 0.10
    nickel = 0.05
    penny = 0.01
    print("Please insert coins.")
    num_of_quarter = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickel = int(input("How many nickels?: "))
    num_of_penny = int(input("How many pennies?: "))
    total = (quarter * num_of_quarter) + (dimes * num_of_dimes) + (nickel * num_of_nickel) + (penny * num_of_penny)
    order_cost = machine_menu[user_order]["cost"]
    if total > order_cost:
        change = round(total - order_cost, 2)
        print(f"Here is ${change} in change.")
        return order_cost
    elif total < order_cost:
        print(f"Sorry that's not enough money. ${'{0:.2f}'.format(total)} refunded.")
        return 0.0
    elif total == order_cost:
        return order_cost


# MAIN
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# INIT VARIABLES
def play(menu, resources, machineMoney=None):
    isContinue = True
    haveResources = True
    coins = None
    machineMoney = machineMoney + 0.00

    while isContinue:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "off":
            print("Coffee machine is now turning off....")
            exit()
        elif order == "report":
            # Show current resource values
            for key in resources:
                if key.lower() == "water" or key.lower() == "milk":
                    print(f"{key.title()}: {resources[key]}ml")
                elif key.lower() == "coffee":
                    print(f"{key.title()}: {resources[key]}g")

            print(f"Money: ${'{0:.2f}'.format(machineMoney)}")
        elif order == "espresso":
            isContinue = check_resources(order)
            if isContinue:
                coins = process_coins(order, menu)
                if coins != 0.00:
                    machineMoney += coins
                else:
                    play(menu, resources, machineMoney)
                use_resources(order, menu, resources)
            else:
                play(menu, resources, machineMoney)
        elif order == "latte":
            isContinue = check_resources(order)
            if isContinue:
                coins = process_coins(order, menu)
                if coins != 0.00:
                    machineMoney += coins
                else:
                    play(menu, resources, machineMoney)
                use_resources(order, menu, resources)
            else:
                play(menu, resources, machineMoney)
        elif order == "cappuccino":
            isContinue = check_resources(order)
            if isContinue:
                coins = process_coins(order, menu)
                if coins != 0.00:
                    machineMoney += coins
                else:
                    play(menu, resources, machineMoney)
                use_resources(order, menu, resources)
            else:
                play(menu, resources, machineMoney)

        else:
            print("Invalid input. Kindly check your input spelling. Thanks!")


machineMoney = 0
play(menu, resources, machineMoney)
