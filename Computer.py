from Core import *

zero = 0

lowD = 1
mediumD = 3
highD = 5

lowA = 2
mediumA = 4
highA = 6


def __one_in_a_row(column, board, player_chip):
    row = lowest_open_spot(column, board)

    if ((column < 6) and (player_chip == board[column + 1][row])): # right
        return True
    if ((column > 0) and (player_chip == board[column - 1][row])): # left
        return True
    if ((row > 0) and (player_chip == board[column][row - 1])): # top
        return True
    if ((row < 5) and (player_chip == board[column][row + 1])): # bottom
        return True

    if ((row > 0) and (column < 6)): # top right
        if (player_chip == board[column + 1][row - 1]):
            return True
    if ((row > 0) and (column > 0)): # top left
        if (player_chip == board[column - 1][row - 1]):
            return True
    if ((row < 5) and (column < 6)): # bottom right
        if (player_chip == board[column + 1][row + 1]):
            return True
    if ((row < 5) and (column > 0)): # bottom left
        if (player_chip == board[column - 1][row + 1]):
            return True

    return False # none found

def __two_in_a_row(column, board, player_chip):
    row = lowest_open_spot(column, board)

    if (column < 5): # right
        if (player_chip == board[column + 1][row] and player_chip == board[column + 2][row]):
            return True
    if (column > 1): #left
        if (player_chip == board[column - 1][row] and player_chip == board[column - 2][row]):
            return True
    if (row > 1): # top
        if player_chip == board[column][row - 1] and player_chip == board[column][row - 2]:
            return True
    if (row < 4): # bottom
        if (player_chip == board[column][row + 1] and player_chip == board[column][row + 2]):
            return True

    if ((row > 1) and (column < 5)): # top right
        if ((player_chip == board[column + 1][row - 1]) and (player_chip == board[column + 2][row - 2])):
            return True
    if ((row > 1) and (column > 1)): # top left
        if ((player_chip == board[column - 1][row - 1])
			and (player_chip == board[column - 2][row - 2])):
            return True
    if ((row < 4) and (column < 5)): # bottom right
        if ((player_chip == board[column + 1][row + 1])
			and (player_chip == board[column + 2][row + 2])):
            return True
    if ((row < 4) and (column > 1)): # bottom left
        if ((player_chip == board[column - 1][row + 1])
		    and (player_chip == board[column - 2][row + 2])):
            return True

    return False # none found

def __three_in_a_row(column, board, player_chip):
    row = lowest_open_spot(column, board)

    if (column < 4): # right
        if (player_chip == board[column + 1][row]
			and player_chip == board[column + 2][row]
			and player_chip == board[column + 3][row]):
            return True
    if (column > 2): # left
        if (player_chip == board[column - 1][row]
			and player_chip == board[column - 2][row]
			and player_chip == board[column - 3][row]):
            return True
    if (row > 2): # top
        if (player_chip == board[column][row - 1]
			and player_chip == board[column][row - 2]
			and player_chip == board[column][row - 3]):
            return True
    if (row < 3): # bottom
        if (player_chip == board[column][row + 1]
			and player_chip == board[column][row + 2]
			and player_chip == board[column][row + 3]): # right
            return True

    if ((row > 2) and (column < 4)): # top right
        if ((player_chip == board[column + 1][row - 1])
			and (player_chip == board[column + 2][row - 2])
			and (player_chip == board[column + 3][row] - 3)):
            return True
    if ((row > 2) and (column > 2)): # top left
        if ((player_chip == board[column - 1][row - 1])
			and (player_chip == board[column - 2][row - 2])
			and (player_chip == board[column - 3][row - 3])):
            return True
    if ((row < 3) and (column < 4)): # bottom right
        if ((player_chip == board[column + 1][row + 1])
			and (player_chip == board[column + 2][row + 2])
			and (player_chip == board[column + 3][row] + 3)):
            return True
    if ((row < 3) and (column > 2)): # bottom left
        if ((player_chip == board[column - 1][row + 1])
			and (player_chip == board[column - 2][row + 2])
			and (player_chip == board[column - 3][row + 3])):
            return True

    return False # none found

def __rating(column, board):
    if (__three_in_a_row(column, board, computer)):
        return highA
    if (__three_in_a_row(column, board, player)):
        return highD
    if (__two_in_a_row(column, board, computer)):
        return mediumA
    if (__two_in_a_row(column, board, player)):
        return mediumD
    if (__one_in_a_row(column, board, computer)):
        return lowA
    if (__one_in_a_row(column, board, player)):
        return lowD
    return zero

def computer_move(board):
    choices = [0]*7
    for i in range(width):
        choices[i] = __rating(i, board)
    max = 0
    for i in range(width):
        if choices[i] > choices[max]:
            max = i
        if (choices[i] == choices[max]) and ((2 < i) and (i < 5)):
            max = i

    board = move(max, "computer", board)
    return board
