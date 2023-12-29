import random
import re
import words
from style import Color, style_colors


def show_title():

    lilac_color = style_colors['lilac']
    game_title = '''
  _    _            _   _   _____  __  __            _   _ 
 | |  | |    /\    | \ | | / ____||  \/  |    /\    | \ | |
 | |__| |   /  \   |  \| || |  __ | \  / |   /  \   |  \| |
 |  __  |  / /\ \  | . ` || | |_ || |\/| |  / /\ \  | . ` |
 | |  | | / ____ \ | |\  || |__| || |  | | / ____ \ | |\  |
 |_|  |_|/_/    \_\|_| \_| \_____||_|  |_|/_/    \_\|_| \_|
                                                           
'''
    formatted_game_title = lilac_color.format(game_title)
    print(formatted_game_title)
    print("Welcome to Hangman Game!")


def show_play_rules():
    """
    Displays the rules if the user chooses to, does nothing otherwise
    """
    pink_color = style_colors['pink']

    display_rules = input("Would you like to see the game rules? (y/n)\n ")
    while display_rules.lower() not in ['y', 'n']:
        display_rules = input('Please only choose n to skip the rules\
                               or y to see them\n')

    if display_rules.lower() == 'y':
        rules = [
            "Insert your username so we know who are playing with.",
            "Choose a difficulty level between easy, medium, and hard.",
            "Choose a letter that you believe is in the word to guess.",
            "A correct letter will show you its position(s) in the word.",
            "A wrong letter would add to the hangman.",
            "You have six tries to guess, otherwise the man will be hanged",
            "Let's begin"
        ]
        print("\nPlaying Rules:")
        for rule in rules:
            formatted_rule = pink_color.format(rule)
            print(f"  - {formatted_rule}")
    else:
        print("\nYou have chosen to skip the rules. Let's start the game.")


def add_a_name():
    """
    It asks the user to enter a name and validates it
    """
    pattern = re.compile("^[a-zA-Z0-9]{1,8}$")

    while True:
        username = input("Please Enter a username:\n ")
        if pattern.match(username):
            print(f"\n{username}, let's start the hangman game! Have fun!")
            break
        else:
            print("\nInvalid username. Please use only letters and numbers, \
                  and the length should be between 1 and 8 characters.")


def choose_difficulty():
    """
    Gets the user to choose the difficulty of the game that they prefer
    """
    while True:
        try:
            print("\nChoose the difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")

            selected_choice = input("\nEnter the number \
                corresponding to your choice:\n ")
            selected_choice = int(selected_choice)
            # Validate user input
            if selected_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.\n")
            break
        except ValueError as e:
            print(e)

    if selected_difficulty == 1:
        return words.easy_level_words
    elif selected_difficulty == 2:
        return words.medium_level_words
    else:
        return words.hard_level_words



def get_random_word(word_list):
    """
    Returns a randomly selected word from the given word list.
    """
    random_word = random.choice(word_list)
    return random_word.upper()

def check_letters(guessed_letters):
    while True:
        try:
            letter = input('Please enter a letter to guess:\n ').upper()
            if len(letter) != 1

def game_play(username):
    while True:
        word_list = choose_difficulty()
        
        guessed_letters = []

