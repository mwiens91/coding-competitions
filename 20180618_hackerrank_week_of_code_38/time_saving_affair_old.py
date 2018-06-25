#!/usr/bin/env python3

import math
import re
import resource
import sys


def find_waiting_time(time):
    """Find how long you have to wait for a light to turn green."""
    global light_delay

    # Find what phase we're in. Non-negative phase means it's red.
    # Otherwise, it's green.
    phase = time % (2 * light_delay) - light_delay

    if phase >= 0:
        return light_delay - phase
    return 0


def breadth_first_search(node, time, parent_node=None):
    """Recursive function to do ~breadth-first search."""
    global adjacency, best_times

    # If the time taken so far is not better than the best possible time
    # to get to the end node, get out
    if best_times[-1] < time:
        return

    # Populate this list as we look at children
    nodes_to_visit_next = []

    # Find the waiting time to get onto the the next edge
    waiting_time = find_waiting_time(time)

    # Visit each child
    for child_node, edge_time in adjacency[node].items():
        # Don't bother going back to the parent node
        if parent_node is not None and child_node == parent_node:
            continue

        # Calculate the total time
        total_time = waiting_time + edge_time + time

        if total_time < best_times[child_node]:
            # Take this route
            best_times[child_node] = total_time
            nodes_to_visit_next.append(child_node)

    # Continue searching at each node we want to go to
    for child_node in nodes_to_visit_next:
        breadth_first_search(child_node, best_times[child_node])


# Recurse forever
resource.setrlimit(resource.RLIMIT_STACK,
                   [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_nodes = int(lines[0])
light_delay = int(lines[1])
num_edges = int(lines[2])
edges = [[int(x) for x in re.split(r'\D', line)] for line in lines[3:]]

# Useful lists to keep track of the graph
adjacency = [{} for i in range(num_nodes)]
best_times = [math.inf for i in range(num_nodes)]
best_times[0] = 0

# Build adjacency list
for edge in edges:
    i, j, t = edge

    # Ignore self-edges
    if i == j:
        continue

    # Use zero-indexing
    i -= 1
    j -= 1

    # Record the edge
    if j not in adjacency[i] or adjacency[i][j] > t:
        adjacency[i][j] = t
        adjacency[j][i] = t

# Perform a search
breadth_first_search(0, 0)

# Print the answer
print(best_times[-1])
