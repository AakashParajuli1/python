import string

capital = list(string.ascii_uppercase)
small = list(string.ascii_lowercase)


def is_valid_password(password):
    has_capital = False
    has_small = False
    has_digits = False
    for i in password:
        if i in capital:
            has_capital = True
        if i in small:
            has_small = True
        if i.isdigit() is True:
            has_digits = True
    return has_capital and has_small  and has_digits and len(password) >= 8


def main():
    password = input("Enter the password: ")
    if is_valid_password(password):
        print("Password valid!!")
    else:
        print("Invalid password")


if __name__ == "__main__":
    main()
