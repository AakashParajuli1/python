import string
str1 = string.digits
str2 = string.ascii_lowercase
str3 = string.ascii_uppercase
password = input("Enter a valid password(at least 1 uppercase, 1 lowercase, 1 digit: ")

while True:

    has_digit = False
    has_lowercase = False
    has_uppercase = False
    has_length = False
    for i in password:
        if i in str1:
            has_digit = True
        if i in str2:
            has_lowercase = True
        if i in str3:
            has_uppercase = True
    if len(password) >= 12:
        has_length = True
    if (has_length and has_digit and has_uppercase and has_lowercase) is True:
        print("The password is valid.")
        break
    else:
        print("Invalid input")
    password = input("Re-enter a valid password(at least 1 uppercase, 1 lowercase, 1 digit: ")
