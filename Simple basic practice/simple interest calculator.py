principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : "))
    if principle < 0:
     print("Principle cannot be less than or equal to zero .")
    else:
        break


while True:
    time = float(input("Enter the time : "))
    if time < 0:
     print("Time cannot be less than or equal to zero .")
    else:
     break

while True:
    rate = float(input("Enter the rate : "))
    if rate < 0:
     print("Rate cannot be less than or equal to zero .")
    else:
        break
print(f"The principle is: ${principle}")
print(f"The time is : {time} years")
print(f"The rate is : {rate} %")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s : ${total:.2f}")