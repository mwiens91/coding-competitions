"""Made disgusting in a bad attempt to optimize. Didn't work :(."""
import sys
import re

def returnneighbours(i, j):
    """Return a list of tuples of neighbour coordinates."""
    coords = []
    for row_ in range(i-1,i+2):
        # Make sure we respect boundaries
        if row_ == -1:
            row_ = rows - 1
        elif row_ == rows:
            row_ = 0

        for col_ in range(j-1,j+2):
            # " "
            if (row_, col_) == (i,j):
                continue

            if col_ == -1:
                col_ = cols - 1
            elif col_ == cols:
                col_ = 0

            coords += [(row_, col_)]

    return coords

def returnalivecoordsandneighbours():
    coords = []
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '*':
                coords += [(i,j)] + returnneighbours(i,j)

    return list(set(coords))

def printboard(board):
    for row in board:
        print(''.join(row))

# Read lines
lines = [line.strip() for line in sys.stdin.readlines()]

# Grab the number of iterations and the board
iterations = int(re.split("[^0-9]", lines[0])[2])
board = [list(line) for line in lines[1:]]

# Grab dimensions
rows = len(board)
cols = len(board[0])

# Next board
nextboard = [['-' for j in range(cols)] for i in range(rows)]
interestingpoints = returnalivecoordsandneighbours()

# Run them iterations
for iter_ in range(iterations):
    newinterestingpoints = []

    # Gen board
    for i in range(rows):
        for j in range(cols):
            nextboard[i][j] = '-'

    for i,j in interestingpoints:
        numalive = 0

        for neighbour in returnneighbours(i,j):
            if board[neighbour[0]][neighbour[1]] == '*':
                numalive += 1

        if board[i][j] == '*':
            if numalive in {2,3}:
                nextboard[i][j] = '*'
                newinterestingpoints += [(i,j)] + returnneighbours(i,j)
        else:
            if numalive == 3:
                nextboard[i][j] = '*'
                newinterestingpoints += [(i,j)] + returnneighbours(i,j)

    for i in range(rows):
        for j in range(cols):
            board[i][j] = nextboard[i][j]

    interestingpoints = list(set(newinterestingpoints))

printboard(board)
