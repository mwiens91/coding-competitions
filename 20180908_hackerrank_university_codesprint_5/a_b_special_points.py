#!/usr/bin/env python3

import sys


def get_all_connected_groups(graph):
    """Thanks to Matias Thayer on StackOverflow for this function!"""
    already_seen = set()
    result = []
    for node in graph:
        if node not in already_seen:
            connected_group, already_seen = get_connected_group(
                node,
                already_seen,
                graph)
            result.append(connected_group)
    return result


def get_connected_group(node, already_seen, graph):
    """Thanks to Matias Thayer on StackOverflow for this function!"""
    result = []
    nodes = set([node])
    while nodes:
        node = nodes.pop()
        already_seen.add(node)
        nodes = nodes or graph[node] - already_seen
        result.append(node)
    return result, already_seen


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input - and zero-index the vertices
num_vertices, _, a, b = [int(i) for i in lines[0].split()]
edges = [[int(i) for i in line.split()] for line in lines[1:]]

# Determine adjacencies for each vertex
adjacency_dict = {i: set() for i in range(1, num_vertices + 1)}

for edge in edges:
    u, v = edge
    adjacency_dict[u].add(v)
    adjacency_dict[v].add(u)

# Count the adjacency of each vertex
adjacency_count = {i: len(adjacencies)
                   for i, adjacencies in adjacency_dict.items()}

# Determine connected components
connected_components = get_all_connected_groups(adjacency_dict)

# Assign a connected component to each vertex
vertex_groups = {}

for component_idx, component in enumerate(connected_components):
    for vertex in component:
        vertex_groups[vertex] = component_idx

# For each group, find the lowest and highest adjacency
component_vals = {}

for component_idx, component in enumerate(connected_components):
    all_adj = [adjacency_count[vertex] for vertex in component]
    component_vals[component_idx] = {
        "min": min(all_adj),
        "max": max(all_adj),
    }

# Now for each vertex, see if it's a,b special
count = 0

for v in range(1, num_vertices + 1):
    if (a * component_vals[vertex_groups[v]]["min"]
            < adjacency_count[v]
            < b * component_vals[vertex_groups[v]]["max"]):
        count += 1

# Print result
print(count)
