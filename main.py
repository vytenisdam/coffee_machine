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

def choice():
    user_choice = input('What would you like? (Espresso, Latte, Cappuccino) ')
    return user_choice

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):


def actions():
    cho = choice()
    if cho == 'report':
        print(resources)
    elif cho == 'espresso':
        espresso()
    elif cho == 'latte':
        latte()
    elif cho == 'cappuccino':
        cappuccino()
    elif cho == 'off':
        print('Coffee machine is now off.')
        exit()

def espresso():
    if resources['water'] >= MENU['espresso']["ingredients"]['water'] and resources['coffee'] >= MENU['espresso']["ingredients"]['coffee']:
        inserted_money = insert_coins()
        if pinigai >= MENU['espresso']['cost']:
            change = inserted_money - MENU['espresso']['cost']
            resources['water'] -= MENU['espresso']["ingredients"]['water']
            resources['coffee'] -= MENU['espresso']["ingredients"]['coffee']
            resources['money'] += MENU['espresso']['cost']
            print(f'Here is your Espresso and there is your change {round(change, 2)}')
        else:
            print(f'Insert more coins, here is your: $ {inserted_money} back.')
    else:
        print('Not enough resources')

def latte():
    if resources['water'] >= MENU['latte']["ingredients"]['water'] and resources['coffee'] >= MENU['latte']["ingredients"]['coffee'] and resources['milk'] >= MENU['latte']["ingredients"]['milk']:
        inserted_money = insert_coins()
        if inserted_money >= MENU['latte']['cost']:
            change = inserted_money - MENU['latte']['cost']
            resources['milk'] -= MENU['latte']["ingredients"]['milk']
            resources['water'] -= MENU['latte']["ingredients"]['water']
            resources['coffee'] -= MENU['elatte']["ingredients"]['coffee']
            resources['money'] += MENU['latte']['cost']
            print(f'Here is your Latte and there is your change {round(change, 2)}')
        else:
            print(f'Insert more coins, here is your: $ {inserted_money} back.')
    else:
        print('Not enough resources')

def cappuccino():
    if resources['water'] >= MENU['cappuccino']["ingredients"]['water'] and resources['coffee'] >= MENU['cappuccino']["ingredients"]['coffee'] and resources['milk'] >= MENU['cappuccino']["ingredients"]['milk']:
        inserted_money = insert_coins()
        if inserted_money >= MENU['cappuccino']['cost']:
            change = inserted_money - MENU['cappuccino']['cost']
            resources['milk'] -= MENU['cappuccino']["ingredients"]['milk']
            resources['water'] -= MENU['cappuccino']["ingredients"]['water']
            resources['coffee'] -= MENU['cappuccino']["ingredients"]['coffee']
            resources['money'] += MENU['cappuccino']['cost']
            print(f'Here is your Cappuccino and there is your change: ${round(change, 2)}')
        else:
            print(f'Insert more coins, here is your: $ {inserted_money} back.')
    else:
        print('Not enough resources')
def insert_coins():
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

going = 'on'

while going != 'off':
        actions()


