#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_students = int(lines[0])
ids_called = [int(x) for x in re.split(r'\D', lines[1])]

# Print the absent students
print(*sorted(list(set(range(1, num_students + 1)) - set(ids_called))))
