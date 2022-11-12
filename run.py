# All code or resources used in this project are credited in the README file.
import random
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


