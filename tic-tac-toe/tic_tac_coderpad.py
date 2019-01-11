#!/usr/bin/python3

import random

###Declarations
board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

num_board = [0,1,2,
             3,4,5,
             6,7,8]


###Functions
def print_board(board):
  print()
  print(board[0], '|', board[1], '|', board[2])
  print('--------')
  print(board[3], '|', board[4], '|', board[5])
  print('--------')
  print(board[6], '|', board[7], '|', board[8])
  print()

def ai_move(board):
    while(True):
        rand_position = random.randint(0,8)
        if (board[rand_position] == ' ' and board[rand_position] != 'X'
            and board[rand_position] != 'O'):
            return rand_position
        
def check_win(board, char):
    if ((board[0] == char and board[1] == char and board[2] == char) or
        (board[3] == char and board[4] == char and board[5] == char) or
        (board[6] == char and board[7] == char and board[8] == char) or
        (board[0] == char and board[3] == char and board[6] == char) or
        (board[1] == char and board[4] == char and board[7] == char) or
        (board[2] == char and board[5] == char and board[8] == char) or
        (board[0] == char and board[4] == char and board[8] == char) or
        (board[2] == char and board[4] == char and board[6] == char)):
        return char
    else:
        return False
    


###Game
while(True):
    print_board(board)
    position = int(input('What position for your next move? '))
    #Check if valid position
    if position in range(0,9) and board[position] == ' ':
        board[position] = 'X'
        if (' ' not in board):
            print("Game is a Tie")
            break
        if (check_win(board, 'X')):
            print_board(board)
            print("X wins!")
            break
        board[ai_move(board)] = 'O'
        if (check_win(board, 'O')):
            print_board(board)
            print("O wins!")
            break
    else:
        print()
        print('Invalid Entry!')
        pass
