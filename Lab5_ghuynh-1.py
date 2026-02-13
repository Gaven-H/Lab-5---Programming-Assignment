"""
Dice Rolling Terms
Gaven Huynh
This code simulates throwing a pair of die.
It will display the value of each die, the sum, as well as the correlating term.
The code will run until the user decides to quit the program.
February 12, 2026
"""

import random

def dice_roll_term(die1, die2):
    total = die1 + die2

    if die1 == 1 and die2 == 1:
        return "Snake Eyes"
    
    elif (die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1):
        return "Ace Caught a Deuce"
    
    elif die1 == 2 and die2 == 2:
        return "Little Joe from Kokomo"
    
    elif (die1 == 1 and die2 == 4) or (die1 == 4 and die2 == 1):
        return "Little Phoebe"
    
    elif (die1 == 2 and die2 == 3) or (die1 == 3 and die2 == 2):
        return "Little Phoebe"
    
    elif die1 == 3 and die2 == 3:
        return "Jimmy Hicks from the Sticks"
    
    elif (die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6):
        return "Six Ace"
    
    elif die1 == 4 and die2 == 4:
        return "Eighter from Decatur"
    
    elif (die1 == 3 and die2 == 6) or (die1 == 6 and die2 == 3):
        return "Nina from Pasadena"
    
    elif (die1 == 4 and die2 == 5) or (die1 == 5 and die2 == 4):
        return "Nina from Pasadena"
    
    elif die1 == 5 and die2 == 5:
        return "Puppy Paws"
    
    elif (die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6):
        return "Six Five no Jive"
    
    elif die1 == 6 and die2 == 6:
        return "Boxcars"
    
    else:
        return "No Special Terms"

while True:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2

    print("\nYou Rolled:")
    print("First Throw:", die1)
    print("Second Throw:", die2)
    print("Dice Sum:", total)

    term = dice_roll_term(die1, die2)
    print("Dice Term:", term)

    while True:
        user_choice = input("\nRoll the Dice again? (Y/N): ").upper()
        if user_choice == 'Y' or user_choice == 'N':
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")