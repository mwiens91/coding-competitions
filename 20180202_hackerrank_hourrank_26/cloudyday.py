#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_towns = int(lines[0])
populations = [int(x) for x in re.split(r"\D", lines[1])]
town_locations = [int(x) for x in re.split(r"\D", lines[2])]
num_clouds = int(lines[3])
cloud_centres = [int(x) for x in re.split(r"\D", lines[4])]
cloud_widths = [int(x) for x in re.split(r"\D", lines[5])]

# Determine which clouds cover which areas
max_position = max(town_locations)
cloud_areas = dict()

for cloud in enumerate(zip(cloud_centres, cloud_widths)):
    for x in range(cloud[1][0] - cloud[1][1], cloud[1][0] + cloud[1][1] + 1):
        if x not in cloud_areas:
            cloud_areas[x] = str(cloud[0])
        else:
            cloud_areas[x] += str(cloud[0])

# For each cloud determine which city only it covers. If more than one
# cloud covers a city, the city is "doomed". If only one cloud covers a
# city, throw the city's cloud and population in the "covered" dict.
covered = dict()
max_population = 0

for town in enumerate(town_locations):
    # Town is not covered. Add to max population now.
    if town[1] - 1 not in cloud_areas:
        max_population += populations[town[0]]
    elif len(cloud_areas[town[1] - 1]) == 1:
        if cloud_areas[town[1] - 1] not in covered:
            covered[cloud_areas[town[1] -1]] = populations[town[0]]
        else:
            covered[cloud_areas[town[1] -1]] += populations[town[0]]
    else:
        # Town is doomed
        pass

# Now remove a cloud and return the answer
if covered:
    print(max_population + sorted(covered.values(), reverse=True)[0])
else:
    print(max_population)
