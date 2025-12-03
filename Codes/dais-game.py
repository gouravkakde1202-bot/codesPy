import random

def roll_two_dice():
    user_input = input("Do you want to roll two dice? (Y/N): ").strip().lower()

    if user_input == 'y':
        dice1 = random.randint(1, 6) 
        
        dice2 = random.randint(1, 6) 
        
        total_sum = dice1 + dice2 
     
        print("-" * 35)
        print(f"Dice 1 rolled: {dice1}")
        print(f"Dice 2 rolled: {dice2}")
        print(f"Total is: {total_sum}")
        print("-" * 35)
        
        roll_two_dice()
        
    elif user_input == 'n':
        print("Thanks for playing! Goodbye.")
        return
        
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        roll_two_dice()

roll_two_dice()