import coffeemachine_art

coffeemachine_art.logo()

MENU={
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

resources={
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0.00
}




def takeOrder(order):
    quaters=int(input("How many quaters??\n"))
    dimes=int(input("How many dimes??\n"))
    nickles=int(input("How many nickles??\n"))
    pennies=int(input("How many pennies??\n"))
    calculation=0.25*quaters+0.1*dimes+0.05*nickles+0.01*pennies

    if calculation < MENU[order]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return

    resources["water"]-=MENU[order]["ingredients"]["water"]
    if "milk" in MENU[order]["ingredients"]:
        resources["milk"]-=MENU[order]["ingredients"]["milk"]
    resources["coffee"]-=MENU[order]["ingredients"]["coffee"]
    resources["money"]+=MENU[order]['cost']
    changes=round(calculation-MENU[order]['cost'],2)
    if changes > 0:
        print(f"Here is your change:${changes}")
    print(f"Here is your {order}. Enjoy!")




while True:
    order=input('What coffee do you want to order?? "latte", "espresso" or "cappuccino"\n').lower()
    if order=='off':
        break
    
    if order=='report':
        print(f"Water:{resources['water']}ml.")
        print(f"Milk:{resources['milk']}ml.")
        print(f"Coffee:{resources['coffee']}g.")
        print(f"Money:${resources['money']}")
        continue

    if order in MENU:
        if resources["water"] < MENU[order]["ingredients"]["water"]:
            print("Sorry, We are out of water")
        elif "milk" in MENU[order]["ingredients"] and resources["milk"] < MENU[order]["ingredients"]["milk"]:
            print("Sorry, We are out of milk")
        elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
            print("Sorry, We are out of coffee")
        else:
            takeOrder(order)
    else:
        print("Invalid order")

print("We are shutting Down. See you Soon.....")