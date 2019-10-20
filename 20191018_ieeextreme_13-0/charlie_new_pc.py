#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Perform each test case
num_cases = int(lines[0])
idx = 1

for _ in range(num_cases):
    # Parse the test case
    budget = int(lines[idx])
    num_components = int(lines[idx + 1])
    component_options = [
        {int(x) for x in options.split()}
        for options in lines[idx + 3 : idx + 3 + num_components]
    ]
    component_options.sort(key=len)

    # Set up index for next test case
    idx += 3 + num_components

    # Solve test case
    option_idx = 1
    old_sums = component_options[0]

    while option_idx < num_components:
        sums = set()

        for s in old_sums:
            for ns in component_options[option_idx]:
                if s + ns <= budget:
                    sums.add(s + ns)

        old_sums = sums
        option_idx += 1

    if old_sums:
        print(max(old_sums))
    else:
        print(0)
