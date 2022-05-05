#!/usr/bin/python

#Author: n4t5ru

#imports for the calculator
from colorama import init, Fore

#Function for addition
def Addition():
    ans = 0
    numbs = int(input('Enter Value: '))
    repeat = 0

    while numbs != 0:
        ans = ans + numbs
        repeat+=1
        numbs = int(input('Enter Value (0 to Calculate): '))
    print(Fore.LIGHTRED_EX+'\nTotal is: '+ str(ans) + '. By Adding '+str(repeat)+' numbers\n'+Fore.RESET)

#Function for subtraction
def Subtraction():
    ans = 0
    numbs = float(input('Enter Value: '))
    repeat = 0
    
    while numbs != 0:
        ans = ans - numbs
        repeat+=1
        numbs = float(input('Enter Value (0 to Calculate): '))
    print(Fore.LIGHTGREEN_EX+'\nTotal is: '+ str(ans) + '. By Subtracting '+str(repeat)+' numbers\n'+Fore.RESET)

#Function for multiplication
def Multiplication():
    ans = 1
    numbs = float(input('Enter Value: '))
    repeat = 0
    
    while numbs != 0:
        ans = ans * numbs
        repeat+=1
        numbs = float(input('Enter Value (0 to Calculate): '))
    print(Fore.LIGHTMAGENTA_EX+'\nTotal is: '+ str(ans) + '. By Multiplying '+str(repeat)+' numbers\n'+Fore.RESET)

#Function for subtraction
def Division():
    ans = 0
    numbs = float(input('Enter Value: '))
    repeat = 0
    
    while numbs != 0:
        ans = ans / numbs
        repeat+=1
        numbs = float(input('Enter Value (0 to Calculate): '))
    print(Fore.LIGHTBLUE_EX+'\nTotal is: '+ str(ans) + '. By Dividing '+str(repeat)+' numbers\n'+Fore.RESET)

#main function
while True:
    print(Fore.LIGHTBLUE_EX+'''
Welcome to Day 5: Calculator Application:
    press A to Add
    press S to Subtract
    press D to Divide
    press M to Multiply
    press Q to quit
    '''+ Fore.RESET)

    menuOpt = input('Enter Option: ')

    if menuOpt != 'Q':
        if menuOpt == 'A':
            Addition()
        elif menuOpt == 'S':
            Subtraction()
        elif menuOpt == 'M':
            Multiplication()
        elif menuOpt == 'D':
            Division()
        else:
            print('Wrong Option. Try again!')
    else:
        print(Fore.YELLOW+'Goodbye!!'+Fore.RESET)
        break