#Heather Stafford
#4/27/18
#matrixDemo.py - lists inside lists

def printBoard(board):
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c])

board = [['a','b','c'],['d','e','f'],['g','h','i']]

printBoard(board)


