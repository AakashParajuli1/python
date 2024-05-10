menu = {"popcorn": 3.00,
        "french fries": 4.00,
        "combo": 9.70,
        "pizza": 2.65,
        "coke": 1.20}
cart = []
total = 0
print("--------------MENU-----------------")
for key, value in menu.items():
    print(f"{key:15} : ${value:>10.2f}")
print("---------------------------------------")

while True:
    food = input("Enter the food you want to order (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("The item is not on the menu!!")
print("--------------MENU-----------------")
for key, value in menu.items():
    print(f"{key:15} : ${value:>10.2f}")

print("----------------Your Order------------------")
for food in cart:
    total += menu.get(food)
    print(food, end="")
print()
print(f"Your total is : ${total: .2f}")
