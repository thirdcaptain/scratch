#!/usr/bin/python3

import os

num_board = ['0','1','2',
             '3','4','5',
             '6','7','8']

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def intro():
    os.system('clear')
    print()
    print()
    print("Welcome to Tic-Tac-Toe!")
    print()
    print()

def instructions():
    print("To play, enter the number position where you would like to go.")
    print("Press 'q' to quit")
    print()

def show(board):
    print(' ', '|',  board[1], '|', board[2])
    print('----------')
    print(board[3], '|',  board[4], '|', board[5])
    print('----------')
    print(board[6], '|',  board[7], '|',  board[8])
    print()

if __name__ == "__main__":
    intro()
    show(num_board)
    instructions()

    #Loop through gameplay
    while(True):
        show(board)
        x = input("Where do you want to go? ")

        valid_list = []
        for i in range(0,9):
            valid_list.append(i)
        print(valid_list)
        input("This is a test")

        #Check for 'q' to quit game
        if int(x) not in valid_list:
            print("x not in rage 0 - 9")
            break

        board[int(x)] = "X"
        print("Your selection is", x)

