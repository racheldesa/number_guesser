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
play_game = 'y'

while play_game == 'y':
    # Prompt user to set range 
    range_min = input("Enter range minimum: ")
    range_max = input("Enter range maximum: ")

    # Generate random number to be guessed
    mystery_num = random.randint(int(range_min), int(range_max))

    # Keep track of number of user guesses
    num_guesses = 0

    # Game state
    game_over = False

    while not game_over:
        user_guess = int(input("Enter guess: "))
        num_guesses += 1

        if user_guess == mystery_num:
            game_over = True
        elif user_guess > mystery_num: 
            print("Too high. Try again.")
        else:   # user_guess < mystery_num
            print("Too low. Try again.")

    # mystery_num has been guessed correctly
    print(f"Correct! You got it in {num_guesses} tries.")

    # Prompt user to play again
    play_game = input("Play again? (y/n): ")
    print('\n')

# User has quit the game
print("Thanks for playing!\n")