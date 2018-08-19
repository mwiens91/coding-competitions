#!/usr/bin/env python3

import re
import sys

FAILURE = 1
SUCCESS = 0


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_queries = int(lines[0])
queries = [[] for i in range(num_queries)]

# Use this to keep track of which line the next query starts at
cursor = 1

for i in range(num_queries):
    # The number of lines to read
    this_num_lines = int(lines[cursor])

    # Read the lines
    for j in range(cursor + 1, cursor + this_num_lines + 1):
        queries[i].append([int(k) for k in re.split(r'\D', lines[j])])

    # Move up the cursor
    cursor += this_num_lines + 1

# Now go through each query and print the answer
for query in queries:
    # Profit we need to make up the next day
    make_up = 0

    for day in query:
        # Actual and estimated profit
        actual, estimated = day

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
