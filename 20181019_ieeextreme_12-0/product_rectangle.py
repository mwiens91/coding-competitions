#!/usr/bin/env python3

import math
import sys
import numpy as np


def maximum_subarray(array):
    """Kadane's algorithm."""
    max_seen = 0
    max_here = 0

    for k in array:
        max_here = max(0, max_here + k)
        max_seen = max(max_seen, max_here)

    return max_seen


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Matrix details
n, _ = [int(i) for i in lines[0].split()]

# Matrix construction variables
A = [int(i) for i in lines[1].split()]
B = [int(i) for i in lines[2].split()]

# Construct the matrix
M = np.outer(A, B)

# Shrink the matrix row-wise until we find the best sum
best_sum = -math.inf

# Let i be the top row, and j be the bottom row
for i in range(n):
    for j in range(i, n):
        # Collapse all columns into a sum
        submatrix = M[i : j + 1, :]
        submatrix_column_sums = submatrix.sum(axis=0)

        # Find the best sum
        best_sum = max(best_sum, maximum_subarray(submatrix_column_sums))

# Print the answer
print(best_sum)
