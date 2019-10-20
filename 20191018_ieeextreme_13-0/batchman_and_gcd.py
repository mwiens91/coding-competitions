#!/usr/bin/env python3

import itertools
import math
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
_, k = [int(x) for x in lines[0].split()]
nums = {int(x) for x in lines[1].split()}

# Count total num unique GCDs
unique_gcds = nums.copy()

if k > 1:
    for cmb in itertools.combinations(nums, 2):
        unique_gcds.add(math.gcd(cmb[0], cmb[1]))

print(len(unique_gcds))
