#!/usr/bin/env python3

import sys


def isDiscoveredCheck(direction_):
    """Check if moving our pawn checks enemy king.

    If direction is positive, then check if a (possible) piece to the
    right of the pawn being moved can check the king. Otherwise, do the
    same check for a piece to the left of the pawn being moved.

    Returns a boolean indicating whether there was a discovered check.

    Very bad use of global variables, but it comes with the territory
    (the territory being programming competition code).
    """
    # Determine the offset for where to find the piece in question
    offset = 1 if direction_ > 0 else -1

    # If the pawn is on the boundary and the direction faces the
    # boundary, then there can be no discovered check
    boundary = board_size if offset == 1 else 0

    if pawn_index == boundary:
        return False

    # Now find if there's a discovered check on the diagonal
    if (king_position[1] + offset * king_position[0] == pawn_index + offset
       and scenario[0][pawn_index + offset] in {'Q', 'B'}):
        # A queen or bishop just had a diagonal open up that
        # contains the enemy king, check if it can kill the king.
        diag_length = abs(king_position[1] - (pawn_index + offset))

        for y in range(2, diag_length):
            # Check if there's a piece in the way
            if scenario[y][(pawn_index + offset) - y * offset]:
                break
        else:
            return True

    # Now find if there's a discovered check on the one possible row
    # where this could occur
    if king_position[0] == 1:
        # The king is on the 1st row with horizontal direction of the
        # offest relative to the pawn
        x = king_position[1] + offset

        while True:
            this_space = scenario[1][x]

            # Look for a piece
            if this_space in {'Q', 'R'}:
                # A queen or rook can attack
                return True
            elif this_space:
                # A piece is blocking the way
                break

            # Check the next space
            if x == boundary:
                break

            x += offset

    # No discovered check
    return False


def numPromotionChecks():
    """Check how many pawn promotions check the enemy king."""
    # Check the 0th row
    if king_position[0] == 0:
        for dx in [1, -1]:
            # Make sure we're not trying to move over the boundary
            boundary = board_size if dx == 1 else 0

            if pawn_index == boundary:
                break

            x = pawn_index + dx

            while True:
                this_space = scenario[0][x]

                # Look for the king
                if this_space == 'k':
                    # Checked!
                    return 2
                elif this_space:
                    # Another piece is blocking the way
                    break

                # Check the next space
                if x == boundary:
                    break

                x += dx

        # King is in the 0th row but blocked by another piece
        return 0

    # Check the pawn's column
    if king_position[1] == pawn_index:
        y = 1

        while True:
            this_space = scenario[y][pawn_index]

            # Look for the king
            if this_space == 'k':
                # Checked!
                return 2
            elif this_space:
                # The king is on the pawn's column but another piece is
                # blocking the way
                return 0

            y += 1

    # Check the pawn's diagonals - right first, then left
    if king_position[0] == king_position[1] - pawn_index:
        # King is on the pawn's right diagonal
        y = 1

        while True:
            this_space = scenario[y][pawn_index + y]

            # Look for the king
            if this_space == 'k':
                # Checked!
                return 2
            elif this_space:
                # The king is on the pawn's right diagonal but another
                # piece is blocking the way
                return 0

            # Check the next space
            y += 1

    # Check the left diagonal
    if king_position[0] == - (king_position[1] - pawn_index):
        # King is on the pawn's left diagonal
        y = 1

        while True:
            this_space = scenario[y][pawn_index - y]

            # Look for the king
            if this_space == 'k':
                # Checked!
                return 2
            elif this_space:
                # The king is on the pawn's left diagonal but another
                # piece is blocking the way
                return 0

            # Check the next space
            y += 1

    # Check knight positions
    if pawn_index > 1:
        if scenario[1][pawn_index - 2] == 'k':
            return 1

    if pawn_index > 0:
        if scenario[2][pawn_index - 1] == 'k':
            return 1

    if pawn_index < board_size - 1:
        if scenario[1][pawn_index + 2] == 'k':
            return 1

    if pawn_index < board_size:
        if scenario[2][pawn_index + 1] == 'k':
            return 1

    # No checks available from promoting pawn
    return 0


# The dimension of the board, 0 indexed
board_size = 7

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Separate the scenarios
num_scenarios = int(lines[0])
scenarios = []

for i in range(num_scenarios):
    scenarios += [[[j if j != '#' else '' for j in line]
                                        for line in lines[1 + i*8:9 + i*8]]]

# Now solve each scenario
for scenario in scenarios:
    # Find position where pawn will be promoted and make the spot on the
    # board where the pawn was empty.
    for idx, positions in enumerate(zip(scenario[0], scenario[1])):
        if positions[1] == 'P' and not positions[0]:
            pawn_index = idx                    # always in 0th row
            scenario[1][pawn_index] = ''        # remove the pawn from 1st row

    # Find position of king
    for rowidx, row in enumerate(scenario):
        try:
            king_position = (rowidx, row.index('k'))
            break
        except ValueError:
            pass

    # Check the diagonal and row where a discovered check can occur: if
    # pawn is to the right of the king, look to the right for a piece to
    # attack with, otherwise look the left.
    direction = pawn_index - king_position[1]

    if direction and isDiscoveredCheck(direction):
        # There is a discovered check - simply count all possible
        # promotions, since all result in check
        print(4)
        continue

    # No discovered check. Count number of promotions that result in
    # check
    print(numPromotionChecks())
