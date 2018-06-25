#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_scenarios = int(lines[0])
scenarios = []

for i in range(num_scenarios):
    scenarios.append([[int(x) for x in re.split(r'\D', line)]
                      for line in lines[1 + 2*i: 3 + 2*i]])

# Solve each scenario
for scenario in scenarios:
    # Unpack vars
    num_students, my_num, num_sections = scenario[0]
    section_placements = scenario[1]

    # Solve the scenario
    sections_sum = 0

    for section_idx, section_placement in enumerate(section_placements):
        sections_sum += section_placement

        if my_num <= sections_sum:
            print(section_idx + 1)
            break
