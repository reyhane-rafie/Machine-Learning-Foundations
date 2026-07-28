# Rock Paper Scissors
# Player vs Computer.
# (No random module if you haven't learned it.)
# Later
# Use
# import random
# ------------

import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:

    player = input("\nChoose rock, paper, or scissors (or type exit): ")
    player = player.lower()

    if player == "exit":
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("Tie!")

    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1

    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1

    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:")
    print("You:", player_score)
    print("Computer:", computer_score)


print("\nGame Over!")
print("Final Score:")
print("You:", player_score)
print("Computer:", computer_score)