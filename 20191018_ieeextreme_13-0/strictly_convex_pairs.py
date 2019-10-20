#!/usr/bin/env python3

# NOTE: Abandoned part way through

from functools import reduce
from math import comb
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
N, M = [int(x) for x in lines[0].split()]
vertices = [[int(x) for x in vertexLine.split()] for vertexLine in lines[1 : 1 + N]]
points = [
    [int(x) for x in pointLine.split()] + [False]
    for pointLine in lines[1 + N : 1 + N + M]
]

num_pairs = 0

for i in range(N):
    # Grab vertices
    v0 = vertices[i - 1]
    v1 = vertices[i]
    v2 = vertices[(i + 1) % (N - 1)]

    # Grab specific coordinates
    x0, x1, x2, y1, y2, y3 = v0[0], v1[0], v2[0], v0[1], v1[1], v2[1]

    # Two cases: edge generates a vertical line, or it doesn't
    if x1 == x2:
        if x0 < x1:
            outside_fn = lambda x: x > x1
        else:
            outside_fn = lambda x: x < x1
    slope = (v2[1] - v1[1]) / (v2[0] - v1[0])
    o

    # Count points
    n = reduce(f, points, 0)

    num_pairs += comb(n, 2)

# Count inner points
num_pairs += comb(reduce(lambda pt: 1 if pt[2] == False else 0, points, 0), 2)

print(num_pairs)
