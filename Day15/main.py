import menu


def resource_check(ingredients):
    """returns true if the resources are enough"""
    for item in ingredients:
        if ingredients[item] >= menu.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """returns total money inserted"""
    print("\nplese enter coins:\n")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def check_transaction(payment, cost):
    """returns true if the payment is verified"""
    if cost <= payment:
        global profit
        profit += cost
        change = round(payment - cost, 2)
        print(f"\nHere is your ${change} in change.")
        return True 
    else:
        print("Sorry that's not enough money. Money refunded!!")
        return False

def make_coffee(ingredients, resource):
    """makes coffee and recalculates the amount of resources"""
    for item in ingredients:
        resource[item]-= ingredients[item]

is_on = True 

profit = 0

while is_on:
    on = input("\nWould you like to make an order?(yes/no): ").lower()
    if on == "report":
        # print("\n".join("{}:\t{}ml".format(k,v) for k,v in menu.resources.items()))
        print(f"\nWater: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")       
        print(f"Coffee: {menu.resources['coffee']}g")        
        print(f"Money: ${profit}")

    elif on == "yes":
        choice = input("\nWhat would you like?(espresso/latte/cappuccino): ").lower()
        drink = menu.MENU[choice]
        if resource_check(drink['ingredients']):
            cost = drink['cost']
            payment = process_coins()
            if check_transaction(payment, cost):
                make_coffee(drink['ingredients'], menu.resources)
                print(f"enjoy your {choice} ☕!!")

    else:
        is_on = False
        