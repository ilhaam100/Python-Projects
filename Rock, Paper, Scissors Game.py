'''Rock, Paper, Scissor Game'''
import random

# Define the options
options = ["rock", "paper", "scissors"]

# Get user to input their choice
user_choice = input("Choose rock, paper, or scissors: ")

# Generate a random choice for the computer
computer_choice = random.choice(options)

# Print the computer's choice
print(f"The computer chose {computer_choice}.")

# Compare the choices and determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose!")
    else:
        print("You win!")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")

