#!/usr/bin/env python3

import re
import sys

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Make a list of lists of the positions of each house on each street
streets = [[int(x) for x in re.split("\D", line)]
             for (idx, line) in enumerate(lines[1:]) if (idx+1) % 2 == 0]

# Now find time for each street
for street in streets:
    street.sort()
    print(street[-1] - street[0])
