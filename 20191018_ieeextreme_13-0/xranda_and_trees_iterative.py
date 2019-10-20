#!/usr/bin/env python3

import sys

# Add to this variable to determine total sum
total = 0


def dfs(start_node, num_vertices):
    global total

    visited = [False] * num_vertices
    bests = []

    # dfs stack
    stack = [(start_node, None)]

    while stack:
        # Pop vertex
        node, root_node = stack.pop()
        visited[node - 1] = True

        # Visit child nodes
        if root_node is None:
            has_children = len(edge_map[node]) > 0
        else:
            has_children = len(edge_map[node]) > 1

        for child_node in edge_map[node]:
            if visited[child_node - 1]:
                continue

            stack.append((child_node, node))

        if root_node is None:
            bests.append(0)
        else:
            bests.append(max(bests[-1], weight_map[tuple(sorted((node, root_node)))]))

        if not has_children:
            total += bests.pop()
        else:
            total += bests[-1]


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse the edges from input. Edge map has a node as key and a list of
# edges as values. Weight map has tuples of two nodes in lexicographic
# order and integers(?) as values.
n_vertices = int(lines[0])
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

for node_key in edge_map:
    dfs(node_key, n_vertices)

# Divide by two because we're counting each node twice
print((total // 2) % (int(1e9) + 7))
