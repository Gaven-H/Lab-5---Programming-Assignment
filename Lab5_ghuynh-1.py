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