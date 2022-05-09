#!/usr/bin/python

#Author: n4t5ru
#Email: hello@nasru.me

import random
import string

# All the required characters for the password
passCharacts = list(string.ascii_letters + string.digits + "!@#$%^&*()-_=+")
passString = list(string.ascii_letters)
passInteger = list(string.digits)
passSymbols = list("!@#$%^&*()-_=+")

def simpleRandPass():

    lenth = input('\nEnter Password Length: ')

    #empty list to store the password
    password = []

    #shuffle the characters
    random.shuffle(passCharacts)

    #add to the empty list
    for lenth in range(lenth):
        password.append(random.choice(passCharacts))

    #one more shufflue for more secure password
    random.shuffle(password)

    newPass = "".join(password)

    return newPass

def complexRandPass():

    passLength = int(input('\nEnter Password Length: '))

    #The complexity of the password
    symbols = int(input('\nHow many symbols to include: '))
    strings = int(input('\nHow many Strings to include: '))
    integer = int(input('\nHow many Integers to include: '))

    count = symbols+strings+integer

    if count > passLength:
        print('Required characters and password limit does not match.')
        return

    password = []

    for i in range(symbols):
        password.append(random.choice(passSymbols))

    for i in range(strings):
        password.append(random.choice(passString))

    for i in range(integer):
        password.append(random.choice(passInteger))

    if count < passLength:
        random.shuffle(passCharacts)
        for i in range(count - passLength):
            password.append(random.choice(passCharacts))
    
    random.shuffle(password)

    newPass = "".join(password)

    return newPass

