#!/usr/bin/env python3

import re
import sys


def solve_case_1():
    """Solves case one of main problem."""
    global array, is_factor, n, m, k

    # Store a counter for how many "good" subarrays we have
    good_count = 0

    # Case (1): k is 0. Go through all contiguous subarrays.
    for start_idx in range(n):
        for this_idx in range(start_idx, n):
            # Test if we have a factor - get out if so
            if is_factor[this_idx] or array[this_idx] == 0:
                good_count += n - this_idx
                break

    return good_count


def solve_case_2():
    """Solves case two of main problem."""
    global array, is_factor, n, m, k

    # Store a counter for how many "good" subarrays we have
    good_count = 0

    # Case (2): k is not 0. Go through all contiguous subarrays.
    for start_idx in range(n):
        # Store the cumulative product of the subarrays starting at
        # start_idx
        prod = 1

        for this_idx in range(start_idx, n):
            # Test if we have a factor - get out if so
            if is_factor[this_idx] or array[this_idx] == 0:
                break

            # Add to product
            prod *= array[this_idx]

            # See if it's good
            if prod % m == k:
                good_count += 1

    return good_count


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input - each query consists of two lists of integers
num_queries = int(lines[0])
queries = []

# Grab each query
for i in range(1, num_queries + 1):
    queries.append([[int(x) for x in re.split(r'\D', line)]
                    for line in lines[2*i-1:2*i+1]])

# Solve each query
for query in queries:
    # Unpack variables - remember that m is prime
    n, m, k = query[0]
    array = query[1]

    # Go through each of the numbers in the array and find any that have
    # m as a factor
    is_factor = [False] * n

    for i in range(n):
        if not array[i] % m:
            is_factor[i] = True

    # Two cases worth distinguishing: (1) k is 0 and (2) k is not 0
    if not k:
        print(solve_case_1())
    else:
        print(solve_case_2())
