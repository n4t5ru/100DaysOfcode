#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: TicTacToe Game

import random

class TicTacToeMulti:
    def __init__(self):
        self.board=[]

    def createBoard(self):
        for x in range(3):
            row = []
            for y in range(3):
                row.append('-')
            self.board.append(row)
    
    def getRandomFirstPlayer(self):
        return random.randint(0,1)

    def fixSpot(self, row, col, player):
        self.board[row][col]= player

    def playerWin (self, player):
        win = None

        n = len(self.board)

        # Checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                 return win

         # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
            
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def boardFull(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swapPlayerTurn(self, player):
        return 'X' if player == 'O' else 'O'

    def showBoard(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.createBoard()

        player = 'X' if self.getRandomFirstPlayer() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.showBoard()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fixSpot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.playerWin(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.boardFull():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swapPlayerTurn(player)

        # showing the final view of board
        print()
        self.showBoard()


# starting the game
theGame = TicTacToeMulti()
theGame.start()
