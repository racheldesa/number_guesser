import random
import math

"""
Game Flow
----------------------------
1. User inputs range (range min & range max)
2. COM selects random int in range
3. User guess
    > user_guess == num ? Game over, display win message + num_guesses
    > user_guess != num ? increment num_guesses, prompt for next user_guess

"""

# Prompt user to set range 
range_min = input("Enter range minimum: ")
range_max = input("Enter range maximum: ")