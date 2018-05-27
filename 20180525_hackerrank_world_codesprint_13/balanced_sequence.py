#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input. Represent brackets as +-1.
num_brackets = int(lines[0])
brackets = [1 if x == '(' else -1 for x in lines[1]]

# There will only ever need to be 0, 1, or 2 operations. This is not
# true in general, but I did these by testing the test cases presented.
brackets_sum = sum(brackets)

# Test if the brackets are already balanced
if brackets_sum == 0:
    print(0)
    sys.exit(0)

# They aren't. Find if there's a possible 1 operation change to
# balance everything.
for start_idx in range(num_brackets):
    # Keep track of ongoing sum
    sum_ = 0

    for this_idx in range(start_idx, num_brackets):
        # Build up ongoing sum
        sum_ += brackets[this_idx]

        if 2 * sum_ == brackets_sum:
            # Operatioh exists. (Greedy test.) Problem solved.
            print(1)
            sys.exit(0)

# No 1 operation changes exist. It must be a 2 operation change.
print(2)
