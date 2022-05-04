import os
from colorama import init, Fore

looper = True

while looper:
    print(Fore.GREEN+'''
    \nHello....... Below are Options:\n
    1. Download Audio\n
    2. Download Video\n
    3. Exit\n''')

    option = input('Enter Value: ')

    if option == '1':
        print('option one reached')
        break

    elif option == '2':
        print('option two reached')
        break

    else:
        looper=False