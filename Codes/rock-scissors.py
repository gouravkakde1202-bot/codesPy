#Rock paper scissors game
import random

user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("You lost,try again!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")