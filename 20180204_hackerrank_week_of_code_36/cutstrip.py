#!/usr/bin/env python3

import math
import re
import sys


def make_best_cut(start, end, parent_idx, isrow=True):
    """Find minimum sum cut in a 1D array.

    If isrow is True, then we're dealing with a row, otherwise we're
    dealing with a column.

    Returns minimum sum.
    """
    global data_matrix, negative_matrix, sum_matrix, k

    # Store the best result
    bestcut = math.inf

    # Loop variable
    j = start

    # Now find the best cut
    while j < end + 1:
        if isrow:
            thiscut_val = data_matrix[parent_idx][j]
        else:
            thiscut_val = data_matrix[j][parent_idx]

        thiscut_length = 1
        local_best = thiscut_val

        while thiscut_length <= k and j + thiscut_length < end + 1:

            if isrow:
                thiscut_val += data_matrix[parent_idx][j + thiscut_length]
            else:
                thiscut_val += data_matrix[j + thiscut_length][parent_idx]

            local_best = min(local_best, thiscut_val)
            thiscut_length += 1

        # Move to next index
        j += 1

        # See if this is best
        bestcut = min(bestcut, local_best)

    return bestcut


def find_matrix_sum(left, right, up, down):
    """Find the maximum sum of the matrix given that we can cut.

    Returns the maximum sum as an integer.
    """
    global sum_matrix

    # Store the best cut
    best = math.inf

    # Find the best row cut, then find the best column cut
    for row_ in range(up, down + 1):
        best = min(best, make_best_cut(left, right, row_, isrow=True))

    for col_ in range(left, right + 1):
        best = min(best, make_best_cut(up, down, col_, isrow=False))

    if up != 0:
        if left != 0:
            return (sum_matrix[down][right]
                    - sum_matrix[up - 1][right]
                    - sum_matrix[down][left - 1]
                    + sum_matrix[up - 1][left - 1]
                    - best)

        # Up is not 0 and but left is 0
        return (sum_matrix[down][right]
                - sum_matrix[up - 1][right]
                - best)
    if left != 0:
        return (sum_matrix[down][right]
                - sum_matrix[down][left - 1]
                - best)

    # Up and left are 0
    return (sum_matrix[down][right]
            - best)

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
rows, cols, k = [int(x) for x in re.split(r'\D', lines[0])]
data_matrix = [[int(val) for val in re.split(r' ', row)] for row in lines[1:]]

# Sum matrix
sum_matrix = [[0 for col in range(cols)] for row in range(rows)]

# Matrix which shows which elements are negative
negative_matrix = [[True if element < 0 else False for element in rows_]
                                                   for rows_ in data_matrix]

# Compute the matrix sums without cutting
sum_matrix[0][0] = data_matrix[0][0]

for row in range(rows):
    if row != 0:
        sum_matrix[row][0] = sum_matrix[row - 1][0] + data_matrix[row][0]

        for col in range(1, cols):
            sum_matrix[row][col] = (sum_matrix[row][col - 1]
                                    + sum_matrix[row - 1][col]
                                    - sum_matrix[row - 1][col - 1]
                                    + data_matrix[row][col])
    else:
        for col in range(1, cols):
            sum_matrix[row][col] = sum_matrix[row][col - 1] + data_matrix[row][col]

# Hold the best result
best_sum = -math.inf

# Go through each sub-matrix and find the maximum sum. [l, r, u, d]idx
# are left, right, up, and down indices, respectively.
for lidx in range(cols - 1):
    for ridx in range(lidx, cols):
        for uidx in range(rows - 1):
            for didx in range(uidx, rows):
                # Find maximum sum for the submatrix
                result = find_matrix_sum(lidx, ridx, uidx, didx)

                if best_sum < result:
                    best_sum = result

# Print final result
print(best_sum)
