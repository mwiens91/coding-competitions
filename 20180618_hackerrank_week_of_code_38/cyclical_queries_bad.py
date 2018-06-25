#!/usr/bin/env python3
"""This code is based upon a misunderstanding of the problem!

Namely, that each original node has at most two other nodes it can
visit. cyclical_queries_old.py does *not* make this assumption.
"""

import re
import sys


def farthest_node(x):
    """Return the furthest node from x.

    Favour more recent nodes in case of a tie.
    """
    global distances_list, changes_list

    max_distance = max(distances_list[x])
    max_indices = [idx for idx, val in enumerate(distances_list[x])
                   if val == max_distance]
    return max(max_indices, key=lambda x: changes_list[x][-1])


def insert_node(x, w):
    """Insert a new node with edge to node x with weight w."""
    global distances_list, changes_list, changes_list_counter, \
           num_initial_nodes

    # Update other node distances
    for idx in range(num_initial_nodes):
        distances_list[idx][x] += w

    # Update the recently changed list
    changes_list[x].append(changes_list_counter)
    changes_list_counter += 1

    # Update the weights list
    weights_list[x].append(w)


def delete_node(x):
    """Delete a node x."""
    global distances_list, changes_list, num_initial_nodes

    # Get the weight of the node
    w = weights_list[x].pop()

    # Update other node distances
    for idx in range(num_initial_nodes):
        distances_list[idx][x] -= w

    # Update the changes list
    changes_list[x].pop()


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_initial_nodes = int(lines[0])
initial_weights = [int(i) for i in re.split(r'\D', lines[1])]
operations = [[int(i) for i in re.split(r'\D', line)] for line in lines[3:]]

# Keep track of things for our graph
distances_list = [[0] * num_initial_nodes for i in range(num_initial_nodes)]
weights_list = [[] for i in range(num_initial_nodes)]
changes_list = [[0] for i in range(num_initial_nodes)]
changes_list_counter = 1

# Track the initial distances
total_sum = sum(initial_weights)

for i in range(num_initial_nodes):
    accumulate_sum = 0

    for j in range(i + 1, num_initial_nodes):
        accumulate_sum += initial_weights[j]

        distances_list[i][j] = accumulate_sum
        distances_list[j][i] = total_sum - accumulate_sum


# Perform each operation. Make sure to zero-index the node numbers
for operation in operations:
    if operation[0] == 1:
        y = farthest_node(operation[1] - 1)
        insert_node(y, operation[2])
    elif operation[0] == 2:
        insert_node(operation[1] - 1, operation[2])
    elif operation[0] == 3:
        y = farthest_node(operation[1] - 1)
        delete_node(y)
    else:
        y = farthest_node(operation[1] - 1)
        print(distances_list[operation[1] - 1][y])
