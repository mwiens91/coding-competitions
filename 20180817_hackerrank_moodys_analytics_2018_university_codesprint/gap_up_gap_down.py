#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
days = int(lines[0])
low = [int(i) for i in re.split(r'\D', lines[1])]
high = [int(i) for i in re.split(r'\D', lines[2])]
close = [int(i) for i in re.split(r'\D', lines[3])]

# Store number of gap up and gap downs
gap_ups = 0
gap_downs = 0

# Determine the number of gap up and gap downs
for day in range(1, days):
    if low[day] > close[day - 1]:
        gap_ups += 1
    elif high[day] < close[day - 1]:
        gap_downs += 1

# Print results
print(gap_ups, gap_downs)
