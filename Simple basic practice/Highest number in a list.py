a = []
b = input("Enter a number(q to quit) :")
a.append(b)
c = input("Enter numbers to add(q to quit) :")

while c.isdigit() is True:
    a.append(c)
    c = input("Enter numbers to add(q to quit) :")
if c == "q" or "Q":
    print(a)

for x in a:
    while x > b:
        b = x

print(f"The highest number is : {b}")
