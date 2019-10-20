#!/usr/bin/env python3

import sys


# Recurse lots
sys.setrecursionlimit(sys.getrecursionlimit())

# The total sum for the solution
total = 0


def dfs(parent_node, node, best):
    global total

    edges = edge_map[node]

    for child_node in edges:
        if child_node == parent_node:
            continue

        dfs(node, child_node, max(best, weight_map[tuple(sorted((node, child_node)))]))

    total += best


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse the edges from input. Edge map has a node as key and a list of
# edges as values. Weight map has tuples of two nodes in lexicographic
# order and integers(?) as values.
edge_map = {}
weight_map = {}

for line in lines[1:]:
    node1, node2, weight = [int(x) for x in line.split()]

    for n1, n2 in ((node1, node2), (node2, node1)):
        if n1 not in edge_map:
            edge_map[n1] = [n2]
        else:
            edge_map[n1] += [n2]

    weight_map[tuple(sorted((node1, node2)))] = weight

# Do a depth first search taking each node as a root
for root_node in edge_map:
    dfs(None, root_node, 0)

# Divide by two because we're counting each node twice
print((total // 2) % (int(1e9) + 7))
