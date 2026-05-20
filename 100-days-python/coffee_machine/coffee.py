import data

flavours = data.flavours
currency = data.coins
machine_capacity = data.machine_capacity

def user_drink_prompt():
    user_drink_validation = False
    valid_drinks= ["espresso","latte","cappuccino"]
    other_function = ["report","off"]
    while not user_drink_validation:
        user_drink = input("What Would you like? (espresso/latte/cappuccino): ").lower()
        if user_drink in valid_drinks :
            user_drink_validation = True
            return user_drink.title()
        elif user_drink  in other_function:
            return user_drink
        else:
            print("Please choose from the menu.")


def coins(user_drink):
    specific_drink = flavours[user_drink]
    cost_specific_drink = specific_drink["cost"]
    c_quarter = currency["quarters"]
    c_dimes = currency["dimes"]
    c_nickles = currency["nickles"]
    c_pennies = currency["pennies"]
    
    quarters = int(input(("How many quarters?: ")))
    dimes = int(input(("How many dimes?: ")))
    nickles = int(input(("How many nickles?: ")))
    pennies = int(input(("How many pennies?: ")))
    print(f"The cost of {user_drink} : {cost_specific_drink}")
    money = (c_quarter * quarters) + (c_dimes*dimes) + (c_nickles * nickles) + (c_pennies * pennies)
    if money >= cost_specific_drink:
        remaining_cost = money - cost_specific_drink
        if remaining_cost > 0:
            print( f"Here is  ${remaining_cost:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    


def flavour_making(userdrink):
    specific_drink = flavours[userdrink]
    ingredients = specific_drink["ingredients"]
    drink_milk = ingredients["Milk"] if "Milk" in ingredients else 0
    drink_water = ingredients["Water"] if "Water" in ingredients else 0
    drink_coffee = ingredients["Coffee"] if "Coffee" in ingredients else 0
    return drink_milk,drink_water,drink_coffee

def is_resource_sufficient(ingredients):
    milk,water,coffee = ingredients
    machine_milk_quantity = machine_capacity["Milk"]
    machine_water_quantity = machine_capacity["Water"]
    machine_coffee_quantity = machine_capacity["Coffee"]
    if water > machine_water_quantity:
        print("Sorry not enough water")
        return False
    if milk > machine_milk_quantity:
        print("Sorry not enough Milk")
        return False
    if coffee > machine_coffee_quantity:
        print("Sorry not enough Coffee")
        return False
    return True

def deduct_resources(drink_ingredients):
    milk, water, coffee = drink_ingredients
    machine_capacity["Water"] -= water
    machine_capacity["Milk"] -= milk
    machine_capacity["Coffee"] -= coffee
def report():
    print(f"Water: {machine_capacity['Water']}ml")
    print(f"Milk: {machine_capacity['Milk']}ml")
    print(f"Coffee: {machine_capacity['Coffee']}g")





coffee_machine_on = True
while coffee_machine_on:
    user_drink = user_drink_prompt()
    if user_drink == "off":
        print("Turning Off Goodbye")
        coffee_machine_on = False
    elif user_drink == "report":
        report()
    else:
        flavour_ingredients = flavour_making(user_drink)
        if is_resource_sufficient(flavour_ingredients):
            payment_successful = coins(user_drink)
            
            if payment_successful:
                deduct_resources(flavour_ingredients)
                print(f"Enjoy your ☕️{user_drink}")

    