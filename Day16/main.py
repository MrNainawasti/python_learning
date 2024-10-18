from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    on = input("\nWould you like to make an order?(yes/no): ").lower()
    if on == "report":
        coffee_maker.report()
        money_machine.report()
    elif on == "yes":
        options = menu.get_items()
        choice = input(f"\nWhat would you like?({options}): ").lower()
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
    else:
        is_on = False

    