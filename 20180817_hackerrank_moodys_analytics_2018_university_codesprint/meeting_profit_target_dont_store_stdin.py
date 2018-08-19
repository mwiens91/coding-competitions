#!/usr/bin/env python3

from sys import stdin

FAILURE = 1
SUCCESS = 0


# Parse input
num_queries = int(stdin.readline())

# Use this to keep track of which line the next query starts at
cursor = 1

for i in range(num_queries):
    # The number of lines to read
    this_num_lines = int(stdin.readline())

    # Profit we need to make up the next day
    make_up = 0

    # Read the days
    for j in range(this_num_lines):
        # Actual and estimated profit
        actual, estimated = [int(k) for k in stdin.readline().split()]

        # Add in the profit we need to make up to the estimated profit
        estimated += make_up

        if actual >= estimated:
            make_up = 0
        else:
            make_up = estimated - actual

    # Print the answer
    if make_up:
        print(FAILURE)
    else:
        print(SUCCESS)
