import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

#variables holding objects from their respective classes
money_machine = money_machine.MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#main program using OOP
machine_on = True
while machine_on:
    rejected_input = True
    while rejected_input:
        rejected_input = False
        machine_input = input(f"Choose a drink: {menu.get_items()} ")   # prompts user for option/drink
        if machine_input == 'off':                                      # turns off machine
            machine_on = False
            print('Powering off machine')
        elif machine_input == 'report':                                 # prints report
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(machine_input)                      # find drinks
            if drink is None:                                           # if drink is not found, go back
                break
            sufficient_resources = coffee_maker.is_resource_sufficient(drink)   # checks for sufficient resources
            if sufficient_resources:
                coffee_maker.make_coffee(drink) if money_machine.make_payment(drink.cost) else None  # makes coffee if






