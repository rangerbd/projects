menu = {
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
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        is_enough = True
        if order_ingredients[item] >= resources[item]:
            print("theres not enough resources")
            is_enough = False
        return is_enough

        



keep_going = True
while keep_going:
    choice = input("what would you like to have? ")
    if choice == "off":
        break
    elif choice == "report":
        for n in resources:
            print(f"the {n} is {resources[n]} ml")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            print("bb")

