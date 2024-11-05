import random
from art import logo

replay = True

def calculate_diff(s_number, g_number, difficult):
    """Calculate the difference between your guess
    and the secret number, depending on the value, it returns the status."""
    if s_number > g_number:
        print("Too low.")
        return difficult -1
    elif s_number < g_number:
        print("Too high")
        return difficult - 1
    else:
        print(f"You got it! Tha answer was {g_number}.")
        return difficult

def game():
    """The main function, it contains the game core"""
    difficulty = 10
    secret_number = random.randint(0, 101)
    guess = None

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a nuber between 1 and 100.")
    difficulty_selection = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_selection == "hard":
        difficulty = 5

    while difficulty > 0 and secret_number != guess:
        print(f"You have {difficulty} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        difficulty = calculate_diff(secret_number, guess, difficulty)

        if difficulty == 0:
            print("You've run out of of guesses, you lose.")
        elif secret_number != guess:
            print("Guess again")

while replay:
    
    game()
    if input("Type 'y' if you want to play again, or 'n' if not: ") == "n":
        replay = False
    else:
        print("\n" * 20)