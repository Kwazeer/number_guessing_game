import random


def generate_number():
    """Generating random number"""
    rand_num = random.randint(1, 100)
    return rand_num


def main():
    while True:
        print("Welcome to the Number Guessing Game\n"
              "I'm thinking of a number between 1 and 100.\n"
              "You have from 3 to 10 chances to guess the correct number.")

        print("Please, select the difficulty level:\n"
              "1. Easy (10 chances)\n"
              "2. Medium (5 chances)\n"
              "3. Hard (3 chances)")

        user_number = int(input('Enter you choice: '))


