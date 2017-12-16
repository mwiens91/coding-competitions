#!/usr/bin/env python3

import re
import sys

FAILURE = "Impossible"
UPLEFT = "UL "  # leave trailing space for future convenience
UPRIGHT = "UR "
DOWNLEFT = "LL "
DOWNRIGHT = "LR "
LEFT = "L "
RIGHT = "R "


def sign(x):
    return 1 if x >= 0 else -1

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Grab the grid size and get starting and final positions
n = int(lines[0])
positions = [int(r) for r in re.split("\D", lines[1])]
start = positions[:2]
end = positions[2:]

# Find vertical and horizontal displacement, dy and dx, from initial to
# final position
dx = end[1] - start[1]
dy = end[0] - start[0]
absdx = abs(dx)
absdy = abs(dy)

# Print failure and exit if vertical displacement is odd
if absdy % 2 == 1:
    print(FAILURE)
    sys.exit(0)

# Now do y-moves
Ny = absdy//2  # number of y moves

# Print failure and exit if horizontal displacement is odd:
# - even horizontal displacement and odd number of vertical jumps fails
# - odd horizontal displacement and even number of vertical jumps fails
if (absdx % 2 == 0 and Ny % 2 == 1) or (absdx % 2 == 1 and Ny % 2 == 0):
    print(FAILURE)
    sys.exit(0)

# Compute number of horizontally opposite y moves we need
if absdx >= Ny:
    oppmoves = 0
else:
    oppmoves = (Ny - absdx)//2

# Determine new x displacement
if not oppmoves:
    dxprime = dx - sign(dx)*Ny
    absdxprime = abs(dxprime)
else:
    dxprime = 0
    absdxprime = 0

# Now do x-moves
Nx = absdxprime//2   # number of x moves

# Spit out the results - use the ordering of moves given in the
# problem's description
resultstring = ""

if dy < 0:
    # Going up
    if dx < 0:
        # Net left displacement
        resultstring += UPLEFT * (Ny - oppmoves)
        resultstring += UPRIGHT * oppmoves
    else:
        # Net right displacement
        resultstring += UPLEFT * oppmoves
        resultstring += UPRIGHT * (Ny - oppmoves)

if dxprime > 0:
    # Going right after jumping vertically
    resultstring += RIGHT * Nx

if dy > 0:
    # Going down
    if dx < 0:
        # Net left displacement
        resultstring += DOWNRIGHT * oppmoves
        resultstring += DOWNLEFT * (Ny - oppmoves)
    else:
        # Net right displacement
        resultstring += DOWNRIGHT * (Ny - oppmoves)
        resultstring += DOWNLEFT * oppmoves

if dxprime < 0:
    # Going left after jumping vertically
    resultstring += LEFT * Nx

# Print results
print(Ny + Nx)
print(resultstring.strip())
