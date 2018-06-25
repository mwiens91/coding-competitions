#!/usr/bin/env python3

import re
import sys


def farthest_node(x):
    """Return the furthest node from x.

    Favour more recent nodes in case of a tie.
    """
    global distances_dict

    max_distance = max(distances_dict[x].values())
    return max([k for k, v in distances_dict[x].items()
                if v == max_distance])


def insert_node(x, w):
    """Insert a new node with edge with weight w to node x."""
    global distances_dict, next_node_id

    # Update other node distances
    for k, v in distances_dict.items():
        if x in v:
            distances_dict[k][next_node_id] = w + distances_dict[k][x]

    # Add the node
    distances_dict[next_node_id] = {next_node_id: 0}
    next_node_id += 1


def delete_node(x):
    """Delete a node x."""
    global distances_dict

    # Remove the node
    distances_dict.pop(x, None)

    # Update other node distances
    for k in distances_dict.keys():
        distances_dict[k].pop(x, None)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_initial_nodes = int(lines[0])
initial_weights = [int(i) for i in re.split(r'\D', lines[1])]
operations = [[int(i) for i in re.split(r'\D', line)] for line in lines[3:]]

# Keep track of things for our graph
next_node_id = num_initial_nodes + 1
distances_dict = {i: {i: 0} for i in range(1, num_initial_nodes + 1)}

# Track the initial distances
total_sum = sum(initial_weights)

for i in range(1, num_initial_nodes + 1):
    accumulate_sum = 0

    for j in range(i + 1, num_initial_nodes + 1):
        # Our nodes are one-indexed, but initial_weights is zero-indexed
        accumulate_sum += initial_weights[j - 2]

        distances_dict[i][j] = accumulate_sum
        distances_dict[j][i] = total_sum - accumulate_sum

# Perform each operation
for operation in operations:
    if operation[0] == 1:
        y = farthest_node(operation[1])
        insert_node(y, operation[2])
    elif operation[0] == 2:
        insert_node(operation[1], operation[2])
    elif operation[0] == 3:
        y = farthest_node(operation[1])
        delete_node(y)
    else:
        y = farthest_node(operation[1])
        print(distances_dict[operation[1]][y])
