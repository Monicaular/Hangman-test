# hangman.py

import random
import re
import words

def def_title():
    game_title = '''
    .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
    | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
    | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
    | |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
    | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
    | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    '''

    print(game_title)
    print("Welcome to Hangman Game!")

def display_rules():
    display_rules = input("Would you like to see the game rules? (y/n)\n ")

    while display_rules.lower() not in ['y', 'n']:
        display_rules = input('Please only choose n to skip the rules or y to see them\n')

    if display_rules.lower() == 'y':
        rules = [
            "Insert your username so we know who are playing with.",
            "Choose a difficulty level between easy, medium, and hard.",
            "Choose a letter that you believe is in the word to guess.",
            "A correct letter will show you its position(s) in the word. A wrong letter would add to the hangman.",
            "You have six tries to guess; otherwise, the man will be hanged.",
            "Let's begin"
        ]
        print("\n".join(rules))
    else:
        print("You have chosen to skip the rules, let's start the game")

def choose_difficulty():
    while True:
        try:
            print("Choose the difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")

            choice = input("Enter the number corresponding to your choice: ")
            choice = int(choice)

            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.\n")

            break
        except ValueError as e:
            print(e)

    if choice == 1:
        return words.easy_level_words
    elif choice == 2:
        return words.medium_level_words
    else:
        return words.hard_level_words

def choose_random_word(word_list):
    return random.choice(word_list).upper()

def hangman():
    def_title()
    display_rules()

    username_pattern = re.compile("^[a-zA-Z0-9]{1,8}$")
    username = input("Please enter a username: ")

    while not username_pattern.match(username):
        print("Invalid username. Please use only letters and numbers, and the length should be between 1 and 8 characters.")
        username = input("Please enter a valid username: ")

    print(f"{username}, let's start the Hangman game! Have fun!")

    word_list = choose_difficulty()
    secret_word = choose_random_word(word_list)
    guessed_word = ["_" for _ in secret_word]
    guessed_letters = []
    tries = 6

    while tries > 0:
        print(words.hangman_graphic[6 - tries])
        print(" ".join(guessed_word))
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            tries -= 1

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
