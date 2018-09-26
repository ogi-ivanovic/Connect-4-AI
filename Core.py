height = 6
width = 7
player = 1
computer = 2

def createBoard():
    board = []
    for i in range(7):
        column = [0]*6
        board.append(column)
    return board

def lowest_open_spot(column, board):
    for i in range(height - 1, -1, -1):
        if(board[column][i] == 0):
            return i
    return -1 # no open spots in given column

def move(column, player, board):
    move_index = lowest_open_spot(column, board)
    if ("player" == player):
        board[column][move_index] = 1 # player makes move
    else:
        board[column][move_index] = 2 # computer makes move

    return board

def print_board(board):
    print('  ', end='')
    for i in range(width):
        print(i, end='')
        print(' ', end='')
    print('\n ', end='')
    print('---------------')
    for i in range(height):
        print('| ',end='')
        for j in range(width):
            print(board[j][i], end='')
            print(' ', end='')
        print('|')
    print(' ---------------')

def __gameTied(board):
    sum = 0
    for i in range(width):
            sum += lowest_open_spot(i, board)
    if sum == (-7):
        return True
    else:
        return False

def __horizCheck(board):
    for i in range(height):
        for j in range(4):
            sum = board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i]
            if (board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i]):
                if sum == 4 or sum ==8:
                    return True
    return False

def __vertCheck(board):
    for i in range(width):
        for j in range(3):
            sum = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            if (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]):
                if (sum == 4 or sum == 8):
                    return True
    return False

def __diagUpCheck(board):
    for i in range(4):
        for j in range(3,height):
            sum = board[i][j] + board[i+1][j-1] + board[i+2][j-2] + board[i+3][j-3]
            if (board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]):
                if (sum == 4 or sum == 8):
                    return True
    return False

def __diagDownCheck(board):
    for i in range(4):
        for j in range(3):
            sum = board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3]
            if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]):
                if (sum == 4 or sum == 8):
                    return True
    return False

def gameCompleted(board):
    if (__gameTied(board) == True):
        return True
    if (__horizCheck(board) == True):
        return True
    if (__vertCheck(board) == True):
        return True
    if (__diagUpCheck(board) == True):
        return True
    if (__diagDownCheck(board) == True):
        return True
    return False
