# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:36:09 2017

@author: mindovermiles262

Codecademy Python

Add a for loop that repeats the guessing and checking part of your game for 
4 turns, like the example above.
At the beginning of each iteration, print "Turn", turn + 1 to let the player 
know what turn they are on.
Indent everything that should be repeated.

"""

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# For testing purposes
#ship_row=2
#ship_col=2

for turn in range(4):
    print(turn + 1)
    try:
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    except NameError:
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

    # Convert guess to index
    guess_row -= 1
    guess_col -= 1
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print_board(board)
        