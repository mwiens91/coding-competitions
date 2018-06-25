#!/usr/bin/env python3

import math
import re
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


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_nodes = int(lines[0])
light_delay = int(lines[1])
num_edges = int(lines[2])
edges = [[int(x) for x in re.split(r'\D', line)] for line in lines[3:]]

# Useful lists to keep track of the graph
nodes = {i: {} for i in range(num_nodes)}
unvisited = {i: math.inf for i in range(num_nodes)}
unvisited[0] = 0
visited = {}
parent = {}

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
    if j not in nodes[i] or nodes[i][j] > t:
        nodes[i][j] = t
        nodes[j][i] = t

# Perform Djikstra's algorithm (thanks to Kumayl Fazal on stackoverflow)
# for the basic implementation of Djikstra's
while unvisited:
    min_node = min(unvisited, key=unvisited.get)

    for neighbour, drive_time in nodes[min_node].items():
        if neighbour not in visited:
            new_distance = (
                unvisited[min_node]
                + find_waiting_time(unvisited[min_node])
                + drive_time)
            if new_distance < unvisited[neighbour]:
                unvisited[neighbour] = new_distance
                parent[neighbour] = min_node

    visited[min_node] = unvisited[min_node]
    unvisited.pop(min_node)

print(visited[num_nodes - 1])
