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

# Build up a list of necessary exchanges
must_pass_to = [None] * num_students
stack = [(heights[0], 0)]

for i in range(1, num_students):
    while stack and stack[-1][0] < heights[i]:
        _, idx = stack.pop()
        must_pass_to[idx] = i

    stack.append((heights[i], i))

# Partition arrays into left and right sub-arrays where last index of
# the left subarray is a maximum of the left subarray.
left_start_idx = 0
last_idx = num_students - 1
total_cost = 0

# Sort the heights to find list of maximums
sorted_heights = sorted([(heights[i], i) for i in range(last_idx + 1)],
                        reverse=True,
                        key=lambda x: x[0])

last_best_height = sorted_heights[0][0]

# Loop variable
max_idx = 0

while True:

    # Find a maximum height in the new left subarray
    while True:
        if max_idx == last_idx + 1:
            # Stopping condition. Print the result.
            print(total_cost + running_cost)
            sys.exit(0)

        max_height, max_height_idx = sorted_heights[max_idx]
        max_idx += 1

        if max_height_idx < left_start_idx:
            continue
        else:
            break

    # If maximum is at start of the array, see if we want to pass to it
    if max_height_idx == left_start_idx:
        this_cost = (last_best_height
                     - heights[left_start_idx]
                     + prices[left_start_idx])

        if this_cost < 0:
            total_cost += this_cost

        last_best_height = heights[left_start_idx]
        left_start_idx += 1
        continue

    # Now compute cost of left subarray
    for k in range(max_height_idx - 1, left_start_idx - 1, -1):
        # Find the best index to pass to
        try:
            # Find the maximum index we must pass to
            max_pass_idx = must_pass_to[k]

            # Choose the minimum cost index that occurs before or at the
            # closest index we need to pass to
            available_idxs = range(k + 1, max_pass_idx + 1)
            costs = [prices[x] + abs(heights[x] - heights[k])
                                                    for x in available_idxs]
            cheapest_cost = min(costs)

            prices[k] += cheapest_cost
        except ValueError:
            # No such best index
            pass

    # Add the cost of dropping from the last height
    prices[left_start_idx] += last_best_height - max_height

    # Add cost to total cost if we have to or if it's beneficial
    if (max_height == last_best_height
       or prices[left_start_idx] < 0):
        total_cost += prices[left_start_idx]

    # Make right subarray new left subarray
    left_start_idx = max_height_idx + 1
    last_best_height = max_height
