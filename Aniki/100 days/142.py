#TODO: 2. Check resources sufficient to makle drink order
#1print report
#2check resources sufficient ?
#3process coins
#4check transaction successful
#5make coffee
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

# TODO: 1. Print report of all coffee machine resources

choice = input("What would you like? (espresso/latte/cappuccino):")
"Please insert coins"
q = int(input("how many quarters?"))
d = int(input("how many dimes?"))
n = int(input("how many nickles?"))
p = int(input("how many pennies?"))
money = q*0.25 + d*0.1 + n*0.05 + p*0.01

#print(type(money))
#print(type(MENU[choice]["cost"]))

if money > MENU[choice]["cost"]:
    difference = money - int(MENU[choice]["cost"])
    print(f"Here is ${difference} in change.")
    print("Here is your " + choice + ". Enjoy!" )

