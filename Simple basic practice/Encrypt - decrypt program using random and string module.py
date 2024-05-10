import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars :  {chars}")
# print(f"Key :  {key}")

# ENCRYPT
normal_text = input("Enter any message you would like to encrypt :")
encrypted_text = ""

for letters in normal_text:
    index = chars.index(letters)
    encrypted_text += key[index]
print(f"normal text = {normal_text } ")
print(f"encrypted text  = {encrypted_text  } ")

# DECRYPT
encrypted_text = input("Enter any message you would like to decrypt :")
normal_text = " "

for letters in encrypted_text:
    index = key.index(letters)
    normal_text += chars[index]

print(f"encrypted text  = {encrypted_text  } ")
print(f"Decrypted text = {normal_text } ")
