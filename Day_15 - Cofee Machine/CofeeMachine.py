# IMPORTS


# FUNCTIONS


# MAIN
MENU = {
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


# TODO 1: PROMPT USER BY ASKING "WHAT WOULD YOU LIKE?" ( ESPRESSO/LATTER/CAPUCCINO).
#  CHECK USER'S INPUT TO DECIDE WHAT TO DO NEXT
#  PROMPT SHOULD SHOW EVERY TIME ACTION HAS COMPLETED. EG ONCE THE DRINK HAS BEEN DISPENSED
#  THE PROMPT SHOULD SHOW AGAIN TO SERVE THE NEXT CUSTOMER



# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
#  a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
#  Your code should end execution when this happens.


