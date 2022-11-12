# All code or resources used in this project are credited in the README file.
import random
import string

from words import word_list
from time import sleep
from hangman import lives_left

class messages:
    red = '\033[91m'
    green = '\033[92m'
    bold = '\033[1m'


def welcome_rules():
    """
    Welcome user to the game
    Display a set of rules for the game
    """
    print('Welcome to Hangman! \n')
    sleep(1)
    print('Try to guess the random word before you get hung. \n')
    sleep(1)
    print('----------------------------------------')
    sleep(1)

def player_nickname():
    """
    Retrieves the player's nickname. It will be used to give a feedback
    """
    global nickname
    while True:
        nickname = input("\nWho's playing today? ")
        if nickname.isalpha():
            break
        print("Please insert only valid letters (A-Z).\n")
    sleep(1)
    print("\nHave fun, " + f"{nickname.capitalize()}!")
    return nickname


def get_word(word_list):
    """
     gets a word from 'words.py' file
     """
    word = random.choice(word_list)
    return word.upper()


def hangman_game():
    """
    function to guess a random word using a single letter
    while counting on the number of lives left
    """

    welcome_rules()
    player_nickname()
    word = get_word(word_list)
    letters_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    letters_guessed = set()  # letters user guesses

    lives = 10

    while len(letters_needed) > 0 and lives > 0:
        print("\nYou've used these letters: ", ' '.join(sorted(letters_guessed)))
        print('\nLives left:', lives, )

        word_guess = [letter if letter in letters_guessed else '_' for letter in word]
        print(messages.green + lives_left[lives])
        print('Current word: ', ' '.join(word_guess))
        print('\n----------------------------------------')

        user_guess = input('\nPlease guess a letter: ').upper()

        if user_guess in alphabet - letters_guessed:
            letters_guessed.add(user_guess)
            if user_guess in letters_needed:
                letters_needed.remove(user_guess)
                print('')

            else:
                lives = lives - 1
                print('\nOps,', user_guess, 'is not in the word.')

        elif user_guess in letters_guessed:
            print("\nYou've guessed this letter already. Please try again.")

        else:
            print("That doesn't work, please type in a valid letter, A-Z.")

    # player is hanged
    if lives == 0:
        print(messages.red + lives_left[lives])
        print(messages.bold + f"Oh no, {nickname.capitalize()}, you've been hanged!")
        print("The word was" + messages.red, word)
    else:
        print(messages.bold + f"Congratulations {nickname.capitalize()}!")
        print("You're right, the word was " + word)

hangman_game()
