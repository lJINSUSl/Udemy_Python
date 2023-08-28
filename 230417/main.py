from logo import MENU
from logo import resources

resources["money"] = 0 #현재 내가 가지고 있는 돈
MENU["espresso"]["ingredients"]["milk"] = 0

def calculate_coins():
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    money = q*0.25 + d*0.1 + n*0.05 + p*0.01

    return float(round(money,2))

def check_item(input):
    if resources["water"] < MENU[input]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] < MENU[input]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] < MENU[input]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True



def action(input):


    print("Please insert coins.")
    #삽입한 돈
    money = calculate_coins()


    if money < float(MENU[input]["cost"]):
        print("Sorry that's not enough money. Money refunded.")
    else:
        if resources["water"] >= MENU[input]["ingredients"]["water"] and resources["coffee"] >= MENU[user_input]["ingredients"]["coffee"] and resources["milk"] >= MENU[user_input]["ingredients"]["milk"]:
            resources["water"] -= MENU[input]["ingredients"]["water"]
            resources["milk"] -= MENU[input]["ingredients"]["milk"]
            resources["coffee"] -= MENU[input]["ingredients"]["coffee"]

            change = money - float(MENU[input]["cost"])
            print(f"Here is ${change} in change.")
            print(f"Here is your {input}. Enjoy!")

            resources["money"] += float(MENU[input]["cost"])
            print(resources["money"])
        else:
            print("Sorry there is not enough water")

on = True

while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == 'report':
        print(resources)
    elif user_input == 'off':
        on = False
    else:
        T =check_item(user_input)
        if T:
            action(user_input)