#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
N, A, B = [int(x) for x in lines[0].split()]

# Develop solution
numbers_in_sequence = []
steps = 0

while N != 0:
    # Count steps. If we've gone on too long, there's no solution
    steps += 1

    if steps > 1e5:
        print("NO")
        sys.exit(0)

    # Determine an element of the sequence
    if A <= N <= B:
        X = N
    elif A <= N - A <= B:
        X = N - A
    elif B < N - A:
        X = B
    else:
        print("NO")
        sys.exit(0)

    N -= X
    numbers_in_sequence += [X]

print("YES")
print(*sorted(numbers_in_sequence))
