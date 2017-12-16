#!/usr/bin/env python3

import re
import sys

# Hardcoding this because everything else is way too slow - these are
# courtesy of Wolfram Alpha
MODFACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880,
                 3628800, 39916800, 479001600, 227020800,
                 178291200, 674368000, 789888000, 428096000,
                 705728000, 408832000, 176640000, 709440000,
                 607680000, 976640000, 439360000, 984000000,
                 584000000, 768000000, 504000000, 616000000,
                 480000000, 880000000, 160000000, 280000000,
                 520000000, 200000000, 200000000, 400000000,
                 200000000, 800000000]

def factorialmod1e9(n):
    """Computes a factorial of a number n mod 1e9."""
    if n >= 40:
        return 0;
    else:
        return MODFACTORIALS[n]

def op1(array, l, r):
    """Implement type 1 operation."""
    for i in range(l, r + 1):
        if array[i] >= 40:
            continue

        array[i] += 1

def op2(array, l, r):
    """Implement type 2 operation."""
    sum_ = 0

    for i in range(l, r+1):
        if array[i] >= 40:
            continue

        sum_ += factorialmod1e9(array[i])

    return sum_ % int(1e9)

def op3(array, i, v):
    """Implement type 3 operation."""
    array[i] = v

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
A = [int(n) for n in re.split("\D", lines[1])]
operations = [[int(x) for x in re.split("\D", op)] for op in lines[2:]]

# Perform operations
for op in operations:
    if op[0] == 1:
        op1(A, op[1] - 1, op[2] - 1)
    if op[0] == 2:
        print(op2(A, op[1] - 1, op[2] - 1))
    if op[0] == 3:
        op3(A, op[1] - 1, op[2])
