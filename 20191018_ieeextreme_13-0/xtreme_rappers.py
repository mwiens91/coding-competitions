#!/usr/bin/env python3

import math
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
K, J = [int(x) for x in lines[0].split()]

# Solve problem
M = max(K, J)
N = min(K, J)

l = M - N

if l > N:
    print(N)
else:
    print(l + math.floor((N - l) / 3 * 2))
