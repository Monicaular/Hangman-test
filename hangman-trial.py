import os, random, words

word_list = words.easy_level_words
word = random.choice(word_list).upper()
random_word = list(len(word) * '_')
guessed_letters = set()
lives = 6
word_guessed = False

def check_letter(letter, word):
    global random_word
    found = False
    for i in range(0, len(word)):
        if letter == word[i]:
            random_word[i] = letter
            found = True
    return found

def guesses_left():
    """
    Function to show the hangman graphics
    """
    os.system("clear")
    print(words.hangman_graphic[6 - lives])
    print(' '.join(random_word))
    print(f"You have {lives} lives")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

while word_guessed == False and lives > 0:
    guesses_left()
    guess = input('Please guess a letter or a word: ').upper()

    if guess == word:
        word_guessed = True
        random_word = list(word)
    elif len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
        guessed_word = check_letter(guess, word)
        guessed_letters.add(guess)
        if not guessed_word:
            lives -= 1
    else:
        lives -= 1  
    guesses_left()

if '_' not in random_word:
    print('Awesome job, you guessed the word!')
else:
    print(f"You failed, the word was {word}")




    