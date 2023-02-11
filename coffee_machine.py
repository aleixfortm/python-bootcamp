#coffee machine program
from test import MENU
from test import resources

profit = 0

def check_requirements(ingredients, current_resources):
    # checks if machine has required ingredients to make the desired coffee
    denied = False
    for ingredient in ingredients:
        if ingredients[ingredient] > current_resources[ingredient]:
            denied = True
            resource_flag = False
            if ingredient == 'water':
                print('Not enough water, come back later.')
                resource_flag = True
            elif ingredient == 'milk' and resource_flag:
                print('Not enough milk, come back later.')
                resource_flag = True
            elif ingredient == 'coffee' and resource_flag:
                print('Not enough coffee, come back later.')
    return denied

def insert_coins(f_price):
    # Prompts user to insert coins and calculates change, if applicable
    fifty_cents = int(input('How many 50 Cent coins? ')) * 0.5
    twenty_cents = int(input('How many 20 Cent coins? ')) * 0.2
    ten_cents = int(input('How many 10 Cent coins? ')) * 0.1
    five_cents = int(input('How many 5 Cent coins? ')) * 0.05
    total_amount = fifty_cents + twenty_cents + ten_cents + five_cents
    print(f"You inserted {total_amount}EUR")
    refunded = False
    if total_amount < f_price:
        print("That's not enough money. Refunding money.")
        f_price = 0
        refunded = True
    else:
        change = round(total_amount - f_price, 1)
        print(f'Here is {change}EUR in change.')
    return f_price, refunded

def subtract_ingredients(ingredients, current_resources):
    # Subtracts resources after coffee has been served
    f_new_resources = {}
    # As some resources do not match (e.g. there is only water and coffee in espresso) we need to check whether
    # they match before subtracting them. Therefore, unchanged ingredients will not be added to the new dictionary
    for i in current_resources:
        for j in ingredients:
            if i == j:
                f_new_resources[i] = resources[i] - ingredients[j]
    return f_new_resources


machine_on = True
while machine_on:
    rejected_input = True
    while rejected_input:
        rejected_input = False
        machine_input = input("\nWhat would you like? (espresso, latte, cappuccino?) ").lower()
        # Different actions depending on user input
        if machine_input == 'off':
            machine_on = False
            print('Powering off machine')
        elif machine_input == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {profit}EUR")
        elif machine_input == 'espresso' or machine_input == 'cappuccino' or machine_input == 'latte':
            required_ingredients = MENU[machine_input]['ingredients']
            price = MENU[machine_input]['cost']
        else:
            rejected_input = True

    # Checks if requirements to make coffee are met
    denied_serving = check_requirements(required_ingredients, resources)
    # If requirements are met, ask to insert coins and sum profits
    if not denied_serving:
        print(f'Price is: {price}EUR')
        gained_money, refund_flag = insert_coins(price)
        if not refund_flag:
            profit += gained_money
            new_resources = subtract_ingredients(required_ingredients, resources)
            print(f"Enjoy your {machine_input}!")
            # Replaces new resource values into resource dictionary
            for i in new_resources:
                resources[i] = new_resources[i]

