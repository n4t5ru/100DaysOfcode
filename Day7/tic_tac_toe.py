#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me

import random
from colorama import init, Fore

class TicTacToeMulti:
    def __init__(self):
        self.board=[]

    def createBoard(self):
        for x in range(3):
            row = []
            for y in range(3):
                row.append('-')
            self.board.append(row)
        