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
        username = input("Please Enter a username: ")
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
                corresponding to your choice: ")
            selected_choice = int(selected_choice)
            # Validate user input
            if selected_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter 1, 2, or 3.\n")
            return selected_choice  # Return the selected choice
        except ValueError as e:
            print(e)


def get_random_word(word_list):
    """
    Returns a randomly selected word from the given word list.
    """
    random_word = random.choice(word_list)
    return random_word.upper()


def check_letters(random_word, guessed_letters, \
                  tries, word_completed, red_color, green_color):
    guess = input("Please guess a letter: ").upper()

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}. Try again.")
        elif guess not in random_word:
            error_message = f"{guess} is not in the word."
            print(red_color.format(error_message))
            guessed_letters.add(guess)
            tries -= 1
        else:
            guess_message = f"Well done, {guess} is in the word."
            print(green_color.format(guess_message))
            guessed_letters.add(guess)
            word_as_list = list(word_completed)
            indices = [i for i, letter in enumerate(random_word) \
                       if letter == guess]

            for index in indices:
                word_as_list[index] = guess

            word_completed = "".join(word_as_list)

            if "_" not in word_completed:
                print(f'Congratulations! You guessed the word: {random_word}')
                return word_completed
    # else:
    #     print("Invalid input. Please enter a single letter.")
    elif not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
    return word_completed


def reveal_word(word_completed, random_word):
    if "_" not in word_completed:
        print(f'Congratulations! You guessed the word: {random_word}')
        return True
    return False


def game_play(random_word):
    red_color = style_colors['pale_red']
    green_color = style_colors['bright_green']
    word_completed = "_" * len(random_word)
    guessed_letters = set()
    tries = 6

    while tries > 0:
        game_state(random_word, guessed_letters, tries)
        word_completed = check_letters(random_word, guessed_letters, \
                                       tries, word_completed, red_color, \
                                       green_color)
        if "_" not in word_completed:
            print(f'Congratulations! You guessed the word: {random_word}')
            break

        tries -= 1
    if tries == 0:
        print(f"Sorry, you're out of tries. The word was: {random_word}")


def game_state(random_word, guessed_letters, tries):
    print(words.hangman_graphic[6 - tries])
    display_word = " ".join([letter if letter \
                            in guessed_letters else "_" for letter \
                            in random_word])
    print(f"Word: {display_word}")
    print(f"You have {tries} tries left")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")


def play_hangman_again():
    while True:
        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing Hangman! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' to play again or\
                  'n' to exit.")


def main():
    show_title()
    show_play_rules()
    add_a_name()
    selected_difficulty = choose_difficulty()

    if selected_difficulty == 1:
        word_list = words.easy_level_words
    elif selected_difficulty == 2:
        word_list = words.medium_level_words
    else:
        word_list = words.hard_level_words

    random_word = get_random_word(word_list)

    print(f"\nSelected difficulty level: {selected_difficulty}")

    game_play(random_word)

    play_hangman_again()


if __name__ == "__main__":
    main()
