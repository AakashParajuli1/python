# Exception handling in python :
try:
    numerator = int(input("Enter a numerator :"))
    denominator = int(input("Enter a denominator :"))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by 0 , you idiot!! ")
except ValueError as e:
    print(e)
    print("Something went wrong in the value")
except Exception:
    print("Exception handling error")
finally:
    print("This will always execute at the end")