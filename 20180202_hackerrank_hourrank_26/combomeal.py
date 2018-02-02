#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
priceslist = [[int(x) for x in re.split(r"\D", line)] for line in lines[1:]]

# Now determine profit
for prices in priceslist:
    print(abs(prices[2] - prices[1] - prices[0]))
