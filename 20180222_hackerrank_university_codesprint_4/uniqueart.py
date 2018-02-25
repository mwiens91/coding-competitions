#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse data
num_paintings = int(lines[0])
painting_types = [int(i) for i in re.split(r' ', lines[1])]
students = [[int(i) - 1for i in re.split(r'\D', line)] for line in lines[3:]]

# From left to right count how many paintings of each type have been
# seen so far
left_sums = [None] * num_paintings
left_sums[0] = {painting_types[0]: 1}

for i in range(1, num_paintings):
    # Copy the dictionary
    left_sums[i] = left_sums[i - 1].copy()

    # Add the painting type
    if painting_types[i] in left_sums[i]:
        left_sums[i][painting_types[i]] += 1
    else:
        left_sums[i][painting_types[i]] = 1

# Now go through each student and print number of unique paintings each
# sees
for student in students:
    # The left and right-most paintings a student sees
    leftidx = student[0]
    rightidx = student[1]

    # Get the painting sums for the painting before the first painting
    # the student sees and the last painting the student sees
    if not leftidx:
        before_paintings = set()
    else:
        before_paintings = set(left_sums[leftidx - 1].keys())

    right_paintings = set(left_sums[rightidx].keys())

    # Find paintings unique to right painting sum not found at the
    # painting right before the left painting sum
    new_paintings = right_paintings.difference(before_paintings)

    # Now for each of the paintings, find out whether it's seen exactly
    # once
    uniques = 0

    for painting in new_paintings:
        if left_sums[rightidx][painting] == 1:
            uniques += 1

    for painting in before_paintings:
        if (left_sums[rightidx][painting]
           - left_sums[leftidx - 1][painting] == 1):
            uniques += 1

    # Print the result
    print(uniques)
