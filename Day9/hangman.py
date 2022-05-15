#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: Hangman Game

import random

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

    print('Missed Letters: ', end=' ')
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