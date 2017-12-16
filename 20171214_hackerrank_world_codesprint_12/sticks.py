#!/usr/bin/env python3

import re
import sys


def highest_prime_factor(n):
    """Credit goes to user44810's answer here:
    https://stackoverflow.com/questions/24166478/efficient-ways-of-finding-the-largest-prime-factor-of-a-number

    This is *slightly* modified for the purposes of this question.
    """
    wheel = [1,2,2,4,2,4,2,4,6,2,6]
    w, f, fs = 0, 2, []
    while f*f <= n:
        while n % f == 0:
            fs.append(f)
            n //= f
        f, w = f + wheel[w], w+1
        if w == 11: w = 3
    if n > 1: fs.append(n)

    if not fs:
        return None
    else:
        return fs[-1]

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Get the length of each of the chocolate bars
lengths = [int(length) for length in re.split("\D", lines[1])]

# Now break and eat the bars
totalmoves = 0

for length in lengths:
    full_length = length
    pieces = 1
    moves = 0

    # Repeatedly divide by highest prime factor
    while True:
        factor = highest_prime_factor(length)

        if factor:
            moves += pieces
            length //= factor
            pieces = full_length // length
        else:
            break

    # Now the length of the pieces are either one or an odd prime
    if length != 1:
        moves += pieces

    # Now count eating and sum it to the total moves
    totalmoves += moves + full_length

# Print final result
print(totalmoves)
