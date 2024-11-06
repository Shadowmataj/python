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

money = 0
turn_off = False

def resources_print():
    global resources
    global money
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} gr")
    print(f"Money: ${money}")

def cup_of_coffe(r_list, coffee, mon, cofee_name):
    enough_resources = True

    for item in coffee["ingredients"]:
        if r_list[item] < coffee["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            enough_resources = False

    if not enough_resources:
        return [r_list, mon]
    print(f"The coffee's cost is ${coffee["cost"]}")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickels = int(input("Nickels: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01

    total_order = quarters + dimes + nickels + pennies

    if total_order < coffee["cost"]:
        print(total_order)
        print("Sorry that's not enough money. Money refunded.")
        return [r_list, mon]
    elif total_order >= coffee["cost"]:
        change = total_order - coffee["cost"]
        total_order -= change
        print(f"Making your coffee, ${round(change,2)} dollars in change.”")

    for item in coffee["ingredients"]:
        r_list[item] -= coffee["ingredients"][item]
    mon += total_order
    print(f"Here is your {cofee_name}. Enjoy!.")
    return [r_list, mon]

while not turn_off:
    option =  input("What would you like? (espresso/latte/cappuccino): ").lower()

    try:
        if option == "report":
            resources_print()
        elif option == "off":
            turn_off = True
        elif MENU[option]:
            list_of_changes = cup_of_coffe(resources, MENU[option], money, option)
            resources = list_of_changes[0]
            money = list_of_changes[1]
    except KeyError:
        print("Invalid selection, try again.")