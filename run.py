import words
import random
import re

def show_title():
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

def show_play_rules():
    """
    Displays the rules if the user chooses to, does nothign otherwise
    """
    display_rules = input("Would you like to see the game rules? (y/n)\n " )
    
    while display_rules.lower()  not in ['y', 'n']:
        display_rules = input('Please only choose n to skip the rules or y to see them\n')
    
    if display_rules.lower() == 'y':
        rules = [
        "Insert your username so we know who are playing with.",
        "Choose a difficulty level between easy, medium and hard.",
        "Choose a letter that you believe it is in the word to guess.",
        "A correct letter will show you its position(s) in the word. A wrong letter would add to the hangman.",
        "You have six tries to guess, otherwise the man will be hanged",
        "Let's begin"
    ]
        print(rules)
    else:
        print("You have chosen to skip the rules, let's start the game")

def add_a_name():
    """
    It asks the user to enter a name and validates it
    """
    pattern = re.compile("^[a-zA-Z0-9]{1,8}$")
    username = input("Please Enter a username: ")
    if pattern.match(username):
        print(f"{username}, let's start the hangman game! Have fun!")
    else:
        print("Invalid username. Please use only letters and numbers, and the length should be between 1 and 8 characters.")
    



# def main():
#     show_title()
#     show_play_rules()
#     add_a_name()

# main()