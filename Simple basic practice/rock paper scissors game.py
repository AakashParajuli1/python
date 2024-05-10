import random
game = ("rock", "paper", "scissors")
is_running = True
while is_running:
    player = None
    computer = random.choice(game)

    while player not in game:
        player = input("Enter your choice (rock, paper, scissors) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("Its a tie.")
    elif player == "rock" and computer == "scissors":
        print("Player won!!")
    elif player == "paper" and computer == "rock":
        print("Player won!!")
    elif player == "scissors" and computer == "paper":
        print("Player won!!")
    else:
        print("Computer won!!!")

    question = input("Would you like to play again? (y/n) : ").lower()
    if not question == "y":
        is_running = False

print("You played great today !!!!")
