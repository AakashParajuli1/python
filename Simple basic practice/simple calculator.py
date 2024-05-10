# very simple calculator:
operator = input("Enter an operator (+, -, *, /, %) :")

num1 = float(input("Enter the 1st number : "))

num2 = float(input("Enter the 2nd number : "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
else:
    print("Enter a valid operator!")

print(f"The answer is : {round(result, 2)}")
