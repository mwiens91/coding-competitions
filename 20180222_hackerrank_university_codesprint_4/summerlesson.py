#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
_, num_classes = [int(i) for i in re.split(r'\D', lines[0])]
classes_freq = [0] * num_classes

# Find the frequencies for which the classes are taken
for idx in re.split(r'\D', lines[1]):
    classes_freq[int(idx)] += 1

# Print the answer
print(*classes_freq)
