#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
seat = int(lines[0])

# Find the berth type
rem = seat % 8

if not rem:
    print("SUB")
elif rem == 7:
    print("SLB")
elif rem in {3, 6}:
    print("UB")
elif rem in {2, 5}:
    print("MB")
else:
    print("LB")
