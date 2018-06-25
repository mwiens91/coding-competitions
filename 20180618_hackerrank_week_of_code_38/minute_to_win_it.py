#!/usr/bin/env python3

import collections
import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
n, k = [int(i) for i in re.split(r' ', lines[0])]
a = [int(i) for i in re.split(r' ', lines[1])]

# Perform ~linear regression
line_transform = [a_i - i*k for i, a_i in enumerate(a)]

# Find count of most points on a line
line_transform_count = collections.Counter(line_transform)
count = line_transform.count(line_transform_count.most_common(1)[0][0])

# Print the answer
print(n - count)
