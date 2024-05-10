# 3. Shopping cart
item = input("What item would You like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?:"))

total = price * quantity

print(f"You have bought {quantity} * {item}")
print(f"Your total is : ${round(total, 2)}")