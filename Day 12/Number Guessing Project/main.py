# "Choose a difficulty. Type 'easy' or 'hard': "
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {answer}")
# You've run out of guesses, you lose.
# You got it. The answer was {random_number}.

import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def choose_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 5
    if level == 'easy':
        attempts = 10
    return attempts

def get_random_number():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    return number

def start_game():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    random_number = get_random_number()
    allowed_attempts = choose_level()
    while allowed_attempts > 0:
        print(f"You have {allowed_attempts} remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        if guess_number == random_number:
            print(f"You got it. The answer was {random_number}.")
            return
        elif guess_number < random_number:
            print("Too low.\nGuess again.")
            allowed_attempts -= 1
        elif guess_number > random_number:
            print("Too high.\nGuess again.")
            allowed_attempts -= 1

        if allowed_attempts == 0:
            print("You've run out of guesses, you lose.")

start_game()
