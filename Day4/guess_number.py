#!/usr/bin/python

#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: Guessing game

import random

#user guess function
def user_guess(num):
    random_number = random.randint(1, num)
    guess = 0

    while num != random_number:
        guess = int(input(f'Guess a Number between 1 and {num}: '))

        if guess<random_number:
            print('Number too Low...')
        elif guess>random_number:
            print('Number is too High..')
        
    print(f'\nYour number({guess}) is correct!!')

#computer guess function
def comp_guess(num):
    lower_bound = 1
    higher_bound = num
    feedback = ''

    while feedback != 'C':
        
        if lower_bound != higher_bound:
            guess = random.randint(lower_bound, higher_bound)
        else:
            guess = lower_bound
            
        feedback = input(f'Is the number {guess}\n"H" too High\n"L" too Low\n"C" Correct!\n')
        
        if feedback == 'h' or 'H':
            higher_bound = guess -1
        elif feedback == 'l' or 'L':
            lower_bound = guess + 1
        else:
            print('\nInvalid Character!')
    print('\nCorrect Answer!!!')

#user menu to interact
looper=True

while looper:
    print('''
Welcome to Guessing Game:
    A) You guess PCs Number
    B) PC guesses Your number
    Q) Exit Game
    ''')

    menuOpt = input('Enter Your Choice: ')
    
    if menuOpt == 'A':
        upper_limit = int(input('\nEnter Upper Bound: '))
        user_guess(upper_limit)
    elif menuOpt == 'B':
        upper_limit = int(input('\nEnter Upper Bound: '))
        comp_guess(upper_limit)
    elif menuOpt == 'Q':
        looper = False
    else:
        print('\nInvalid Character!')