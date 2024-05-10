user = int(input("Enter a number:"))
print(f"MULTIPLICATION TABLE FOR '{user}'")
for x in range(1, 11):
    print(f"{user} * {x} = {user * x}")
