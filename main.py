import random


def chose_difficulty(user_input):
    """Filtrating difficulty from user input"""
    if user_input == '1':
        return 'Great! You have selected Easy difficulty level'
    elif user_input == '2':
        return 'Great! You have selected Medium difficulty level'
    elif user_input == '3':
        return 'Great! You have selected Hard difficulty level'
    else:
        return 'There is no such difficulty! Try again.'


def generate_number():
    """Generating random number"""
    num = random.randint(1, 100)
    return num


def game_start():
    print("\nWelcome to the Number Guessing Game\n"
          "I'm thinking of a number between 1 and 100.\n"
          "You have from 3 to 10 chances to guess the correct number.\n")

    print("Please, select the difficulty level:\n"
          "1. Easy (10 chances)\n"
          "2. Medium (5 chances)\n"
          "3. Hard (3 chances)\n")

    user_number = input('Enter you choice (number): ')
    print(chose_difficulty(user_number))


def main():
    game_start()

    while True:
        gen_num = generate_number()


main()
