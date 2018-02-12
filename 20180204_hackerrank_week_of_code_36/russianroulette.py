#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Maximum number of unlocks is the number of locked doors
n = int(lines[0])
max_unlocks = lines[1].count('1')

# Minimum number of unlocks is the number of consecutive pairs of locked
# doors with no overlap, plus the remaining locked doors
doors_list = [int(door) for door in re.split(r'\D', lines[1])]

i = 0
pairs = 0

while i < n - 1:
    if (doors_list[i]
       and doors_list[i + 1]):
        i += 2
        pairs += 1
    else:
        i += 1

min_unlocks = max_unlocks - pairs

# Print answer
print("%d %d" % (min_unlocks, max_unlocks))
