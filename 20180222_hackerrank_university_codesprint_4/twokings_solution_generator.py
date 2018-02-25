#!/usr/bin/env python3
"""A (messy) script to brute force solution to the two kings problem.

I'm writing most of this at way-too-late at night and . . . I don't
know. It's sloppy as hell. Don't judge me based only on this.
"""

import base64
import pickle


def find_N_queen_solns(king1, king2, N):
    """Finds N queen solutions."""
    global positions

    for queen1pos in positions:
        if queen1pos == king1 or queen1pos == king2:
            continue

        for queen2pos in positions:
            if (queen2pos == king1
               or queen2pos == king2
               or queen2pos == queen1pos):
                continue

            if N >= 3:
                for queen3pos in positions:
                    if (queen3pos == king1
                       or queen3pos == king2
                       or queen3pos == queen1pos
                       or queen3pos == queen2pos):
                        continue

                    if N >= 4:
                        for queen4pos in positions:
                            if (queen4pos == king1
                               or queen4pos == king2
                               or queen4pos == queen1pos
                               or queen4pos == queen2pos
                               or queen4pos == queen3pos):
                                continue

                            if N == 5:
                                for queen5pos in positions:
                                    if (queen5pos == king1
                                       or queen5pos == king2
                                       or queen5pos == queen1pos
                                       or queen5pos == queen2pos
                                       or queen5pos == queen3pos
                                       or queen5pos == queen4pos):
                                        continue

                                    if check_solution(king1,
                                                      king2,
                                                      queen1pos,
                                                      queen2pos,
                                                      queen3pos,
                                                      queen4pos,
                                                      queen5pos):
                                        return (queen1pos,
                                                queen2pos,
                                                queen3pos,
                                                queen4pos,
                                                queen5pos)

                            else:
                                if check_solution(king1,
                                                  king2,
                                                  queen1pos,
                                                  queen2pos,
                                                  queen3pos,
                                                  queen4pos):
                                    return (queen1pos, queen2pos, queen3pos, queen4pos)

                    else:
                        if check_solution(king1,
                                          king2,
                                          queen1pos,
                                          queen2pos,
                                          queen3pos):
                            return (queen1pos, queen2pos, queen3pos)
            else:
                if check_solution(king1,
                                  king2,
                                  queen1pos,
                                  queen2pos):
                    return (queen1pos, queen2pos)

    return False

def check_solution(king1, king2, queen1, queen2, queen3=None, queen4=None, queen5=None):
    """Checks if a solution is valid."""
    king1positions = []
    king2positions = []

    if queen5:
        queenpositions = (queen1, queen2, queen3, queen4, queen5)
    elif queen4:
        queenpositions = (queen1, queen2, queen3, queen4)
    elif queen3:
        queenpositions = (queen1, queen2, queen3)
    else:
        queenpositions = (queen1, queen2)

    for king in [king1, king2]:
        for dx in [-1, 0, 1]:
            if king[1] + dx < 0 or king[1] + dx > 7:
                continue

            for dy in [-1, 0, 1]:
                if king[0] + dy < 0 or king[0] + dy > 7:
                    continue

                newpos = (king[0] + dy, king[1] + dx)

                if king == king1 and newpos != king2:
                    king1positions.append(newpos)
                elif king == king2 and newpos != king1:
                    king2positions.append(newpos)

    for pos in king1positions:
        if not check_position(pos, (king2,), queenpositions):
            return False

        if not check_position(king2, (pos,), queenpositions):
            return False

    for pos in king2positions:
        if not check_position(pos, (king1,), queenpositions):
            return False

        if not check_position(king1, (pos,), queenpositions):
            return False

    return True

def check_position(pos, kingpositions, queenpositions):
    """Checks if a position is in check."""
    # Check row
    for x in range(pos[1] + 1, 8):
        if (pos[0], x) in kingpositions:
            break
        elif (pos[0], x) in queenpositions:
            return True

    for x in range(pos[1] - 1, -1, -1):
        if (pos[0], x) in kingpositions:
            break
        elif (pos[0], x) in queenpositions:
            return True

    # Check column
    for y in range(pos[0] + 1, 8):
        if (y, pos[1]) in kingpositions:
            break
        elif (y, pos[1]) in queenpositions:
            return True

    for y in range(pos[0] - 1, -1, -1):
        if (y, pos[1]) in kingpositions:
            break
        elif (y, pos[1]) in queenpositions:
            return True

    # Check diagonals
    i = 1
    while pos[0] + i < 8 and pos[1] + i < 8:
        if (pos[0] + i, pos[1] + i) in kingpositions:
            break
        elif (pos[0] + i, pos[1] + i) in queenpositions:
            return True

        i += 1

    i = 1
    while pos[0] + i < 8 and pos[1] - i > -1:
        if (pos[0] + i, pos[1] - i) in kingpositions:
            break
        elif (pos[0] + i, pos[1] - i) in queenpositions:
            return True

        i += 1

    i = 1
    while pos[0] - i > -1 and pos[1] + i < 8:
        if (pos[0] - i, pos[1] + i) in kingpositions:
            break
        elif (pos[0] - i, pos[1] + i) in queenpositions:
            return True

        i += 1

    i = 1
    while pos[0] - i > -1 and pos[1] - i > -1:
        if (pos[0] - i, pos[1] - i) in kingpositions:
            break
        elif (pos[0] - i, pos[1] - i) in queenpositions:
            return True

        i += 1

    return False

# Hold the solution in this
SOLUTIONS = dict()

# Generate possible positions
positions = []

for i in range(8):
    for j in range(8):
        positions.append((i, j))

# Generate a solution for each position
for king1idx in range(32):
    # Update progress on terminal
    print("\n-- progress: %.2f%% --\n" % (king1idx / 32 * 100))

    king1pos = positions[king1idx]

    # Calculate 1/2. We can figure out the other half by symmetry.
    for king2idx in range(king1idx + 1, 64):
        king2pos = positions[king2idx]

        # Try to find a queen solution
        for N in range(2, 7):
            # N = 6 not currently implemented
            if N == 6:
                raise ValueError

            soln = find_N_queen_solns(king1pos, king2pos, N)

            if soln:
                # Log to the terminal
                print("%s %s => %s" % (king1pos, king2pos, soln))

                # Record the solution
                SOLUTIONS[(king1pos, king2pos)] = soln
                break

# Write solutions to a file
with open('solutions.pickle', 'wb') as f:
    f.write(base64.b64encode(pickle.dumps(SOLUTIONS)))
