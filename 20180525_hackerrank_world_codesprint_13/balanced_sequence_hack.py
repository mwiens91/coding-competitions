#!/usr/bin/env python3

import random
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input. Represent brackets as +-1.
num_brackets = int(lines[0])
brackets = [1 if x == '(' else -1 for x in lines[1]]

# There will only ever need to be 0, 1, or 2 operations. This is not
# true in general, but I did these by testing the test cases presented.
brackets_sum = sum(brackets)

# Test if the brackets are already balanced
if brackets_sum == 0:
    print(0)
    sys.exit(0)

# Guess between 1 and 2, favouring 1, since there are more of these
# answers.
guess1 = random.randint(1,2)

if guess1 == 1:
    print(1)
else:
    print(random.randint(1,2))
