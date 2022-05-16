#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: Hangman Game

from ast import For
import random
import string
from colorama import Fore

Hangman_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow \
    deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole \
        monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark \
            sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# This function will return random string from the passed list
def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(Hangman_pics[len(missedLetters)])
    print()

    print('\nMissed Letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # Show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure that the player entered a single letter only

    while True:
        guess = input('\nGuess a letter: ').lower()

        if len(guess) != 1:
            print('\nPlease Enter one Letter at a time.\n')

        elif guess in alreadyGuessed:
            print('\nYou have already Guessed the letter.\n')
        
        elif guess not in string.ascii_lowercase:
            print('\nEnter a LETTER!!\n')
        
        else:
            return guess

# This function will return True if player wants to play or else False
def playAgain():
    again = input('\nPlay Again? (Yes or No): ').lower()

    return again.startswith('y')

print(Fore.RED+'\nWelcome to HANGMAN!!'+Fore.RESET)

# Global Variables
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(Fore.GREEN+f'\nYou guessed {secretWord} Correctly!!'+Fore.RESET)
            gameDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(Hangman_pics)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(Fore.LIGHTBLUE_EX+f'\nYou Ran out of guesses.\nAfter {len(missedLetters)} missed Guesses and {len(correctLetters)} correct guesses.\nThe Correct word is {secretWord}'+Fore.RESET)
            gameDone = True

    if gameDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameDone = False
            secretWord = getRandomWord(words)

        else:
            print(Fore.CYAN+'\nGOODBYE!!\n'+Fore.RESET)
            break
