#!/usr/bin/env python3
"""Thanks to Daniel Ray for his write up about weight job scheduling."""

import sys


def binary_search(stars_list, start_idx):
    # Initialize our pointers
    low = 0
    high = start_idx - 1

    # Find the desired star
    while low <= high:
        mid = (low + high) // 2

        if stars_list[mid][1] <= stars_list[start_idx][0]:
            if stars_list[mid + 1][1] <= stars_list[start_idx][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1

    return None


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
num_stars = int(lines[0])
stars = [[int(i) for i in line.split()] for line in lines[1:]]

# Monkey patch the finish times
for star in stars:
    star[1] += 0.1

# Reorder the stars
stars = sorted(stars, key=lambda x: x[1])

# Store our results
results = [0] * num_stars
results[0] = stars[0][2]

# Use DP to find max desirability
for idx in range(1, num_stars):
    # Desirability adding in current star
    desirability_sum = stars[idx][2]
    idx2 = binary_search(stars, idx)

    if idx2 is not None:
        desirability_sum += results[idx2]

    # Compare and choose max desirability
    results[idx] = max(desirability_sum, results[idx - 1])

# Print answer
print(results[num_stars - 1])
