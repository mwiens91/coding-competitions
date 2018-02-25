#!/usr/bin/env python3
"""This is a *greedy* solution whose purpose is to score a few points.
It's not correct!"""

import re
import sys


# Maximum board edge length
MAX_LENGTH = int(3e5)

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
rectangles = [[int(i) for i in re.split(r'\D', line)] for line in lines[1:]]

# Store the occupied rows and columns
occupied_rows = set()
occupied_cols = set()
row_count = 0
col_count = 0

# Fill in the two lists just created
for rectangle in rectangles:
    for i in range(rectangle[0], rectangle[2] + 1):
        if i not in occupied_cols:
            col_count += 1
            occupied_cols.add(i)

    for j in range(rectangle[1], rectangle[3] + 1):
        if j not in occupied_rows:
            row_count += 1
            occupied_rows.add(j)

# Find out whether it's cheaper to erase all rows or all columns
if row_count < col_count:
    print(row_count)
    print(0)
    print()
    print(row_count)
    print(*occupied_rows)
else:
    print(col_count)
    print(col_count)
    print(*occupied_cols)
    print(0)
    print()
