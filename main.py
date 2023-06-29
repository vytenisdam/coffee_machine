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
    "money": 0,
}

#def on_off():
    #keep_going = input('If you would like to turn off, type "off"')
    #return keep_going
def choice():
    user_choice = input('What would you like? (espresso, latte, cappuccino, report)')
    return user_choice

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):


def actions():
    cho = choice()
    if cho == 'report':
        print(resources)
    elif cho == 'espresso':
        espresso()
    elif cho == 'off':
        print('off')
        exit()


def espresso():
    if resources['water'] >= MENU['espresso']["ingredients"]['water'] and resources['coffee'] >= MENU['espresso']["ingredients"]['coffee']:
        pinigai = insert_coins()
        if pinigai >= MENU['espresso']['cost']:
            change = pinigai - MENU['espresso']['cost']
            resources['water'] -= MENU['espresso']["ingredients"]['water']
            resources['coffee'] -= MENU['espresso']["ingredients"]['coffee']
            print(f'here and there is your change {change}')
        else:
            print('insert more money')

    else:
        print('not enough')

def latte():
    if resources['water'] >= MENU['latte']["ingredients"]['water'] and resources['coffee'] >= MENU['latte']["ingredients"]['coffee'] and resources['milk'] >= MENU['latte']["ingredients"]['milk']:
        print('here')

    else:
        print('not enough')

def cappuccino():
    if resources['water'] >= MENU['cappuccino']["ingredients"]['water'] and resources['coffee'] >= MENU['cappuccino']["ingredients"]['milk'] and resources['milk'] >= MENU['cappuccino']["ingredients"]['coffee']:
        print('here')

    else:
        print('not enough')
def insert_coins():
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total



# TODO 2. turn the coffee machine off, by typing 'off' in the promt.user_choice = choice()
going = 'on'

while going != 'off':
        actions()
        #going = on_off()
#insert_coins()
# TODO 3. print report what does the coffee machine has in it.  water/milk/coffee/money.

# TODO 4. Check if the resources in coffee machine is sufficient for selected coffee type.

# TODO 5. If resources are sufficient prompt user to insert coins. quarter - 0.25 dime 0.10 nickel - 0.05 penny - 0.01.

# TODO 6. Calculate monetary value and check if >= to selected coffee price. Offer change if inserted too much.

# TODO 7. If resources are sufficient and money are enough deduct the ingridients from the mashine and make coffe and add money to coffe mashine while giving user the selectedd coffee.

