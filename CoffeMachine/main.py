import data

resources = data.resources
MENU = data.MENU

# tok programa:
# kada se pokrene program postavlja pitanje sta korisnik zeli. Moze da bira: espresso/latte/cappuccino/report/off
# pre kreiranja napitka program treba da proveri da li ima dovoljno sirovina
# ako nema dovoljno ispise "Sorry there is not enough water/milk/coffee."
# ako ima ispise "Please insert coins." i postavlja pitanje koloko kojih novcica korisnik unosi i onda ih sabere
# ako nije dovoljno uneo ispise da "Sorry that's not enough money. Money refunded." i vraca se na pocetak
# ako je uneo dovoljno program kreira napitak i korisniku vraca kusur: "Here is $2.45 dollars in change." pa ispise "Here is your {espresso/latte/cappuccino} ☕. Enjoy!"
# ako je kreirao napitak onda treba da smanji i sirovine

# What would you like? (espresso/latte/cappuccino): => espresso/latte/cappuccino/report/off
# Please insert coins.
    # How many quarters?    - 0.25
    # How many dimes?       - 0.10
    # How many nickles?    - 0.05
    # How many pennies?    - 0.01
# Here is ${iznos} in change. - kusur
# Here is your {espresso/latte/cappuccino} ☕. Enjoy!
# Sorry there is not enough water/milk/coffee.
# report:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

def get_report(p_resources, p_money):
    print(f"Water: {p_resources['water']}ml")
    print(f"Milk: {p_resources['milk']}ml")
    print(f"Coffee: {p_resources['coffee']}g")
    print(f"Money: ${p_money}")

def make_coffee(p_resources, coffee):

    is_enough_resources, message = check_resources(p_resources, coffee)
    if not is_enough_resources:
        print(message)
        return False

    money_paid = get_money()
    if money_paid - coffee["cost"] < 0.0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_paid - coffee["cost"], 2)
        print(f"You paid ${money_paid}, here is ${change} in change.")
        return True

def check_resources(p_resources, coffee):
    water = p_resources["water"] - coffee["ingredients"]["water"]
    milk_needed = coffee["ingredients"].get("milk") or 0
    milk = p_resources["milk"] - milk_needed
    coffee = p_resources["coffee"] - coffee["ingredients"]["coffee"]
    ingredients = []
    if water < 0: ingredients.append("water")
    if milk < 0: ingredients.append("milk")
    if coffee < 0: ingredients.append("coffee")

    if len(ingredients) > 1:
        message = "Sorry there is not enough " + ", ".join(ingredients[:-1]) + " and " + ingredients[-1] + "."
        return False, message
    elif len(ingredients) == 1:
        message = "Sorry there is not enough " + ingredients[0] + "."
        return False, message

    return True, None


def update_resources(p_resources, coffee):
    p_resources["water"] -= coffee["ingredients"]["water"]
    p_resources["milk"] -= coffee["ingredients"].get("milk") or 0
    p_resources["coffee"] -= coffee["ingredients"]["coffee"]
    return p_resources


def get_money():
    print("Please insert coins.")
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    p = int(input("How many pennies? "))
    amount = round(0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p, 2)
    return amount

def turn_on_machine(p_resources, p_menu):
    turn_on = True
    money = 0.0

    while turn_on:
        task = input("What would you like? Enter espresso, latte, cappuccino, report or off: ").lower()
        if not(task == "espresso" or task == "latte" or task == "cappuccino" or task == "report" or task == "off"):
            print("Sorry, that is not a valid option. Choose: espresso, latte, cappuccino or report.")
            continue

        if task == "off":
            turn_on = False
            continue

        if task == "report":
            get_report(p_resources, money)
            continue

        if task != "report":
            coffee = p_menu[task]
            coffee_is_made = make_coffee(p_resources, coffee)
            if coffee_is_made:
                print(f"Here is your {task} ☕. Enjoy!")
                p_resources = update_resources(p_resources, coffee)
                money += coffee["cost"]
            continue

turn_on_machine(resources, MENU)