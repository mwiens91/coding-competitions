#!/usr/bin/env python3

import copy
import re
import resource
import sys


# Recurse forever
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

# Constants
EMPTY = 0
FULL = 1

class BruteForceError(Exception):
    pass

def brute_force_outer_rows(board, next_coord, placements=[]):
    global n, m

    # Find next empty spot
    this_coord = None
    for row in range(next_coord[0], n):
        start_col = next_coord[1] if row == next_coord[0] else 0

        for col in range(start_col, m):
            if board[row][col] == EMPTY:
                this_coord = (row, col)
                break

        if this_coord:
            break

    # Success case
    if not this_coord:
        return placements

    # Lay a piece horizontally
    if (this_coord[1] != m - 1
       and board[this_coord[0]][this_coord[1] + 1] == EMPTY):
        # Mark the piece and put down the next one
        try:
            new_board = copy.deepcopy(board)
            new_placements = placements[:]

            new_board[this_coord[0]][this_coord[1]] = FULL
            new_board[this_coord[0]][this_coord[1] + 1] = FULL
            new_placements += [[this_coord[0], this_coord[1],
                                this_coord[0], this_coord[1] + 1]]

            if this_coord[1] == m - 2:
                new_next_coord = (this_coord[0] + 1, 0)
            else:
                new_next_coord = (this_coord[0], this_coord[1] + 2)

            return brute_force_outer_rows(
                   new_board,
                   new_next_coord,
                   new_placements)
        except BruteForceError:
            pass

    # Lay a piece vertically
    if (this_coord[0] != n - 1
       and board[this_coord[0] + 1][this_coord[1]] == EMPTY):
        # Mark the piece and put down the next one
        new_board = copy.deepcopy(board)
        new_placements = placements[:]

        new_board[this_coord[0]][this_coord[1]] = FULL
        new_board[this_coord[0] + 1][this_coord[1]] = FULL
        new_placements += [[this_coord[0], this_coord[1],
                            this_coord[0] + 1, this_coord[1]]]

        if this_coord[1] == m - 1:
            new_next_coord = (this_coord[0] + 1, 0)
        else:
            new_next_coord = (this_coord[0], this_coord[1] + 1)

        # Let an exception be raised here
        return brute_force_outer_rows(
               new_board,
               new_next_coord,
               new_placements)

    # It's a failure
    raise BruteForceError


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
n, m, x, y = [int(i) for i in re.split(r'\D', lines[0])]

# Make the grid
grid = [[EMPTY] * m for i in range(n)]
grid[0] = [FULL] * x + [EMPTY] * (m - x)
grid[-1] = [EMPTY] * (m - y) + [FULL] * y

# Brute force a solution for the 3 or 4 outer rows. We can figure out
# the rest with symmetry (provided we have time).
try:
    # Print the solution
    soln = brute_force_outer_rows(copy.deepcopy(grid), (0, x))

    # Make the solutions 1-indexed
    for s in enumerate(soln):
        for n in enumerate(s[1]):
            soln[s[0]][n[0]] += 1

    print("YES")
    print(len(soln))

    for domino in soln:
        print(*domino)
except BruteForceError:
    print("NO")
