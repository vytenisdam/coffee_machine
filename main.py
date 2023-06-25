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
user_choice = input('What would you like? (espresso, latte, cappuccino, report)')

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):

# TODO 2. turn the coffe mashine off, by typing 'off' in the promt.
while user_choice != 'off':
    user_choice = input('What would you like? (espresso, latte, cappuccino, report)')
# TODO 3. print report what does the coffee mashine has in it.  water/milk/coffee/money.

# TODO 4. Check if the resources in coffee mashine is sufficient for selected coffee type.

# TODO 5. If resources are sufficient prompt user to insert coins. quarter - 0.25 dime 0.10 nickel - 0.05 penny - 0.01.

# TODO 6. Calculate monetary value and check if >= to selected coffee price. Offer change if inserted too much.

# TODO 7. If resources are sufficient and money are enough deduct the ingridients from the mashine and make coffe and add money to coffe mashine while giving user the selectedd coffee.



else:
    exit()

