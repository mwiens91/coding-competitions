#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
n, k = [int(i) for i in lines[0].split()]
nums = [int(i) for i in lines[1].split()]

# Find the answer
count = 0

for i in range(n):
    xor = nums[i]

    if xor < k:
        count += 1

    for j in range(i + 1, n):
        xor ^= nums[j]

        if xor < k:
            count += 1

# Print the result
print(count)
