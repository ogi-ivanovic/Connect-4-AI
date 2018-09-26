from Player import *
from Computer import *

def play_game():
    print('You are 1\'s, the computer is 2\'s')
    player_name = input('Enter your name: ')

    board = createBoard()

    winner = ""

    print_board(board)

    while True:
        board = player_move(board)

        if gameCompleted(board):
            winner = "player"
            break

        board = computer_move(board)
        print_board(board)
        print('The computer took a turn') # change this wording AF

        if gameCompleted(board):
            winner = "computer"
            break

    if winner == "player":
        print(player_name, ' won!')
    else:
        print(player_name, ' lost! :(')

play_game()
