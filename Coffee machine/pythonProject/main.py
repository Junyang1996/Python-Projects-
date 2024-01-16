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

# global variable for holding the cash in the register
money = 0

# TODO  5. Process coins.
#    a. If there are sufficient resources to make the drink selected, then the program should
#    prompt the user to insert coins.
#    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_payment():
    print("Please insert coins. ")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    monetary_value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return monetary_value


# TODO  6. Check transaction successful?
#    a. Check that the user has inserted enough money to purchase the drink they selected.
#    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#    program should say “Sorry that's not enough money. Money refunded.”.
#    b. But if the user has inserted enough money, then the cost of the drink gets added to the
#    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#    Water: 100ml
#    Milk: 50ml
#    Coffee: 76g
#    Money: $2.5
#    c. If the user has inserted too much money, the machine should offer change.
def valid_transaction(coffee_name, payment):
    """coffee_name is the name of the coffee type, e.g. latte"""
    price = MENU[coffee_name]["cost"]
    global money
    if payment > price:

        print(f"Here is ${round((payment - price), 2)} in change.")
        print(f"Here is your {coffee_name} ☕️. Enjoy!")
        dispense_drinks(coffee_name)
        money += payment
    elif payment == price:
        print(f"Here is your {coffee_name} ☕️. Enjoy!")
        dispense_drinks(coffee_name)
        money += payment
    else:
        print("Sorry that's not enough money. Money refunded.")


def dispense_drinks(coffee_name):
    resources['water'] -= MENU[coffee_name]["ingredients"]['water']

    if "milk" in MENU[coffee_name]["ingredients"]:
        resources['milk'] -= MENU[coffee_name]["ingredients"]["milk"]
    resources['coffee'] -= MENU[coffee_name]["ingredients"]["coffee"]

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#    a. Check the user’s input to decide what to do next.
#    b. The prompt should show every time action has completed, e.g. once the drink is
#    dispensed. The prompt should show again to serve the next customer.


exit_program = False

while not exit_program:
    next_move = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if next_move == "report":
        # TODO 3. Print report.
        #    a. When the user enters “report” to the prompt, a report should be generated that shows
        #    the current resource values. e.g.
        #    Water: 100ml
        #    Milk: 50ml
        #    Coffee: 76g
        #    Money: $2.5
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

    elif next_move == "espresso" or next_move == "latte" or next_move == "cappuccino":
        # TODO  4. Check resources sufficient?
        #    a. When the user chooses a drink, the program should check if there are enough
        #    resources to make that drink.
        #    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        #    not continue to make the drink but print: “Sorry there is not enough water.”
        #    c. The same should happen if another resource is depleted, e.g. milk or coffee.
        if MENU[next_move]["ingredients"]["water"] > resources['water']:
            print("Sorry there is not enough water.")
        elif "milk" in MENU[next_move]["ingredients"] and MENU[next_move]["ingredients"]["milk"] > resources['milk']:
                print("Sorry there is not enough milk.")
        elif MENU[next_move]["ingredients"]["coffee"] > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            valid_transaction(next_move, process_payment())

    elif next_move == "off":
        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        #    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        #    the machine. Your code should end execution when this happens.
        exit_program = True


