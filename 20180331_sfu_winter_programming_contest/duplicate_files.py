#!/usr/bin/env python

from __future__ import division, print_function

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
num_tests_remaining = int(lines[0])
test_cases = []
next_line = 1

while num_tests_remaining:
    # Get number of lines for this test case
    num_lines = int(lines[next_line])
    next_line += 1

    # Get the test case
    test_cases.append(lines[next_line:next_line + num_lines])

    # Set up for next iteration
    num_tests_remaining -= 1
    next_line += num_lines

# Go through each test case
for test in test_cases:
    # Store lowest id per file key here
    file_dict = dict()

    # Go through each id and file key
    for line in test:
        key, value = re.split(' ', line)
        value = int(value)

        if key not in file_dict or file_dict[key] > value:
            file_dict[key] = value

    # Print all the id values in ascending order
    print(*sorted(file_dict.values()))
