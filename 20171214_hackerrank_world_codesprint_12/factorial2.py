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

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
n = [int(n) for n in re.split("\D", lines[0])][0]
A = [int(n) for n in re.split("\D", lines[1])]
operations = [[int(x) for x in re.split("\D", op)] for op in lines[2:]]

# Perform operations
for idx, op in enumerate(operations):
    # Test for type 2 operation
    if op[0] == 2:
        # Perform type 2 operation
        sum_ = 0

        # Iterate through relevant numbers
        for numindex in range(op[1], op[2] + 1):
            count = 0

            # Iterate through previous operations
            for i in range(idx - 1, -1, -1):
                thisop = operations[i]
                opnum = thisop[0]

                # Track operations
                if opnum == 1:
                    if numindex > thisop[2] or numindex < thisop[1]:
                        continue

                    count += 1
                elif opnum == 3:
                    if numindex != thisop[1]:
                        continue

                    count += thisop[2] - 1
                    break

            sum_ += factorialmod1e9(count + 1)

        print(sum_ % int(1e9))
