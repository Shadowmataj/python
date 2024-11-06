import random
from art import logo, vs
from game_data import data

keep_playing = True

def choice_person():
    """Return one option from the data file."""
    return random.choice(data)

def higher_followers(a,b):
    """Return the higher"""
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b

def game():
    """main game"""
    score = 0
    correct_answer = True
    a_person = None
    b_person = None
    print(logo)
    while correct_answer:

        if score == 0:
            a_person = choice_person()
        b_person = choice_person()
        while a_person == b_person:
            b_person = choice_person()

        print(f"Compare A: {a_person["name"]}, {a_person["description"]}, from {a_person["country"]}")
        print(vs)
        print(f"Compare B: {b_person["name"]}, {b_person["description"]}, from {b_person["country"]}")
        answer = input("Who has more followers? Type 'A' or 'B': ")

        if answer.lower() == "a":
            answer = a_person
        else:
            answer = b_person

        higher = higher_followers(a_person, b_person)

        print("\n" * 20)
        if answer == higher:
            score += 1
            a_person = b_person
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            correct_answer = not correct_answer

while keep_playing:
    #use the main function to begin the game.
    game()

    if input("Type 'y' to play again, 'n' to quit: ").lower() == "n":
        keep_playing = False
        print("\n"*20)
