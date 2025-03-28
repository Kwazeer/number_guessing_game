import random


def choose_difficulty(user_input):
    """Filtrating difficulty from user input"""
    if user_input == '1':
        print("\nGreat! You have selected Easy difficulty level\n"
              "Let's start the game!")
        return 10
    elif user_input == '2':
        print("\nGreat! You have selected Medium difficulty level\n"
              "Let's start the game!")
        return 5
    elif user_input == '3':
        print("\nGreat! You have selected Hard difficulty level\n"
              "Let's start the game!")
        return 3
    else:
        print("\nThere is no such difficulty! Try again.")
        new_input = input('Enter you choice (number): ')
        return choose_difficulty(new_input)


def generate_number():
    """Generating random number"""
    num = random.randint(1, 100)
    return num


def game_start():
    """Basic information about the game"""

    print("\nWelcome to the Number Guessing Game\n"
          "I'm thinking of a number between 1 and 100.\n"
          "You have from 3 to 10 chances to guess the correct number.\n")

    print("Please, select the difficulty level:\n"
          "1. Easy (10 chances)\n"
          "2. Medium (5 chances)\n"
          "3. Hard (3 chances)\n")

    user_number = input('Enter you choice (number): ')
    return user_number


def main():
    """Initializing the game"""
    user_input = game_start()
    difficulty = choose_difficulty(user_input)
    rand_num = generate_number()

    attempt_count = 1

    while True:
        num_input = int(input('\nEnter your guess: '))

        if attempt_count == difficulty:
            return 'Incorrect! Not enough attempts! Start again.'
        elif num_input < rand_num:
            attempt_count += 1
            print(f'Incorrect! The number is greater than {num_input}.')
        elif num_input > rand_num:
            attempt_count += 1
            print(f'Incorrect! The number is less than {num_input}.')
        elif num_input == rand_num:
            return f'Congratulations! You guessed the correct number in {attempt_count} attempts.'


result = main()
print(result)
