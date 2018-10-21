#!/usr/bin/env python3

import sys

NO_SOLUTION = "!OK"


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Get the number of test cases
num_test_cases = int(lines[0])

for i in range(num_test_cases):
    # Parse the input for this test case
    S, _ = [int(i) for i in lines[1 + 2 * i].split()]
    num_array = [int(i) for i in lines[2 + 2 * i].split()]

    # Degenerate case
    if len(num_array) < 2:
        print(NO_SOLUTION)
        continue

    # Keep track of the numbers we've seen
    nums_seen = {num_array[0]}

    for num in num_array[1:]:
        # Do we have what we want?
        want = S - num

        if want in nums_seen:
            print(min(num, want), max(num, want))
            break

        nums_seen.add(num)
    else:
        print(NO_SOLUTION)
