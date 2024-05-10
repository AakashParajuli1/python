import random
r = random.randint(1, 100)
guesses = 0
h_num = 0
l_num = 100
while True:
    guess = int(input("Enter your guess :"))
    guesses += 1
    if guess > h_num:
        h_num = guess

    if guess < l_num:
        l_num = guess

    if guess == r:
        print("Your guess is right. You've won!!!!")
        break
    elif guess > r:
        print("your guess is higher than the number.")
    else:
        print("your guess is lower than the number.")

    print(f"The highest guess was : {h_num}")

    print(f"The lowest guess was : {l_num}")

print(f"The correct number was : {r}")
