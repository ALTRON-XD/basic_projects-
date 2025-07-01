import random # Number guessing game

number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
guess = None # Initialize guess to None
attempts = 0 # Initialize attempts to 0

print("Welcome to the Number Guessing Game!") # Welcome message
print("I'm thinking of a number between 1 and 100.") # Instructions for the game

while guess != number_to_guess: # Loop until the correct gues
    guess = int(input("Enter your guess: ")) # Get user input
    attempts += 1 # Increment attempts

    if guess < number_to_guess: # Check if guess is too low
        print("Too low! Try again.")
    elif guess > number_to_guess: # Check if guess is too high
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
