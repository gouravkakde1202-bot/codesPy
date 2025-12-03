import random

def roll_dice():
    user_input = input("Do you want to roll the dice? (Y/N): ").strip().lower()

    if user_input == 'y':
        dice_result = random.randint(1, 6) 
        
        print("-" * 25)
        print(f"You rolled a: {dice_result}")
        print("-" * 25)
        roll_dice()
        
    elif user_input == 'n':
        print("Thanks for playing! Goodbye.")
        return 
        
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        roll_dice()
roll_dice()
