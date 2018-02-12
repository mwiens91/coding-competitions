#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_students = int(lines[0])

# Handle trivial case before continuing parsing
if num_students == 1:
    print(1)
    sys.exit(0)

start_height = int(lines[1])
heights = [start_height] + [int(height) for height in re.split(r'\D', lines[2])]
prices = [0] + [int(price) for price in re.split(r' ', lines[3])]

# Running cost - constant for all baton passing choices
running_cost = num_students

# This will eventually hold a list of cost choices we need to minimize
summed_costs = prices[:]

# Build up a list of necessary exchanges
must_pass_to = [None] * num_students
stack = [(heights[0], 0)]

for i in range(1, num_students):
    while stack and stack[-1][0] < heights[i]:
        _, idx = stack.pop()
        must_pass_to[idx] = i

    stack.append((heights[i], i))

# Go through the heights and prices in reverse order and find the cost
# of each necessary exchange
for i in range(num_students - 2, -1, -1):
    # Find the best index to pass to
    try:
        # Find the maximum index we must pass to
        if must_pass_to[i] is None:
            max_pass_idx = num_students - 1
            pass_required = False
        else:
            max_pass_idx = must_pass_to[i]
            pass_required = True

        # Choose the minimum cost index that occurs before or at the
        # closest index we need to pass to
        available_idxs = range(i + 1, max_pass_idx + 1)
        costs = [(summed_costs[x] + abs(heights[x] - heights[i]), x)
                                                       for x in available_idxs]
        cheapest_cost, cheapest_idx = min(costs, key=lambda x: x[0])

        if not pass_required:
            # Don't have to pass if not beneficial
            if cheapest_cost > 0:
                continue

        summed_costs[i] += (summed_costs[cheapest_idx]
                                     + abs(heights[cheapest_idx] - heights[i]))
    except ValueError:
        # No such best index
        pass

# We start with the first baton carrier, so we must choose that one, and
# it contains the cost for its whole trip
cost = summed_costs[0] + running_cost

# Print result
print(cost)
