from Core import *

def player_move(board):
    column = int(input('Enter a column: '))
    while True:
        if (column < 0) or (column > 6):
            print('You must enter a number between 0 and 6.')
            column = int(input('Enter a column: '))
        else:
            break
    board = move(column, "player", board)
    return board
