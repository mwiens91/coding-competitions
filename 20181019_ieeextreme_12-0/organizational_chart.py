#!/usr/bin/env python3

import sys


class Node:
    """A node representing a division."""

    def __init__(self, name, parent, attr1, attr2):
        """Setup."""
        # Use the nodes dictionary
        global nodes

        self.name = name

        # Parent
        if parent == "NONE":
            self.parent = None
        else:
            self.parent = parent

        # Children
        self.children = []

        # Attribute 1
        if attr1 == 0:
            self.attr1_min = None
            self.attr1_max = None
        else:
            self.attr1_min = attr1
            self.attr1_max = attr1

        # Attribute 2
        if attr2 == 0:
            self.attr2_min = None
            self.attr2_max = None
        else:
            self.attr2_min = attr2
            self.attr2_max = attr2

    def __str__(self):
        """String representation."""
        info = self.name + " children:"

        for child in self.children:
            info += "  %s" % child

        if not self.children:
            info += "  none"

        return info


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
N, Q = [int(i) for i in lines[0].split()]

nodes = {}
queries = []

for line in lines[1 : N + 1]:
    # Parse the line
    line_parts = line.split()
    node_name = line_parts[0]
    parent_name = line_parts[1]
    attr1 = int(line_parts[2])
    attr2 = int(line_parts[3])

    # Add the node
    nodes[node_name] = Node(node_name, parent_name, attr1, attr2)

    # Mark this as a child for its parent node
    if parent_name != "NONE":
        nodes[parent_name].children.append(node_name)

# Build up the list of queries

for line in lines[N + 1 : N + Q + 1]:
    line_parts = line.split()

    queries.append([line_parts[0], int(line_parts[1])])

# Clean up variables we don't need anymore
del N, Q, line

# Might come back to this later. Current algorithm in mind almost
# certainly not efficient enough.
for node in nodes.values():
    print(node)
