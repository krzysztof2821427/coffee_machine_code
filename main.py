

from menu import MENU, resources

money_in_machine = 0
money_to_return = 0

should_machine_works = True


def is_enough_and_sell(drink, water, milk, coffee, cost):
    global money_in_machine
    if cost <= money_in_machine:
        if (resources["water"] >= water) and (resources["milk"] >= milk) and (resources["coffee"] >= coffee):
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            print(f"Here is your {drink} ☕ Enjoy!")
        else:
            print("It's not enough resources.")
    else:
        print("You don't have enough money!")



def insert_coins():
    global money_in_machine
    print("Please insert coins.")
    money_in_machine += 0.25 * float(input("How many quarters?: "))
    money_in_machine += 0.1 * float(input("How many dimes?: "))
    money_in_machine += 0.05 * float(input("How many nickles?: "))
    money_in_machine += 0.01 * float(input("How many pennies?: "))
    print(money_in_machine)


def to_return(cost):
    global money_in_machine
    global money_to_return
    money_to_return = money_in_machine - cost
    money_in_machine -= money_to_return
    print(f"Here is your ${round(money_to_return, 2)}")


print(resources, " ", money_in_machine)  # To delete

while should_machine_works == True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if "report" in choice:
        print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money_in_machine}"""
              )
    elif "espresso" in choice:
        insert_coins()
        is_enough_and_sell("espresso", 50, 0, 18, 1.5)
        to_return(1.5)
        print(resources, " ", round(money_in_machine, 2))  # To delete

    elif "latte" in choice:
        insert_coins()
        is_enough_and_sell("latte", 200, 150, 24, 2.5)
        to_return(2.5)
        print(resources, " ", round(money_in_machine, 2))  # To delete
    elif "cappuccino" in choice:
        insert_coins()
        is_enough_and_sell("cappuccino", 250, 100, 24, 3.0)
        to_return(3.0)
        print(resources, " ", round(money_in_machine, 2))  # To delete
    elif "off" in choice:
        print("Switching off.")
        should_machine_works = False



