text = input("Enter a string:").lower().replace(" ", "")
rev_text = text[::-1]
if text == rev_text:
    print("The given string is palindrome.")
else:
    print("The given string is not palindrome.")
