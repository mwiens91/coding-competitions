#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input - subtract one from each node so we can index by 0
n = int(lines[0])
R = [int(r) for r in re.split("\D", lines[1])]
edges = [sorted([int(x)-1 for x in re.split("\D", edge)]) for edge in lines[2:]]

# Build the tree
tree = dict()
for edge in edges:
    if edge[0] in tree.keys():
        tree[edge[0]].append(edge[1])
    else:
        tree[edge[0]] = [edge[1]]

print(tree)

# What do I do here?
