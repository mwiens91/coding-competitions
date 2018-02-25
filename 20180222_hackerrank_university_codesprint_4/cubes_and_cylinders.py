#!/usr/bin/env python3

import math
import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_packages, num_containers = [int(i) for i in re.split(r'\D', lines[0])]
package_edge_lengths = [int(i) for i in re.split(r'\D', lines[1])]
package_copies = [int(i) for i in re.split(r'\D', lines[2])]
container_radii = [int(i) for i in re.split(r'\D', lines[3])]
container_capacities = [int(i) for i in re.split(r'\D', lines[4])]

# Sort package lists according to decreasing edge length
package_edge_lengths, package_copies = (
            map(list, zip(*sorted(zip(package_edge_lengths, package_copies),
                                  reverse=True))))

# Calculate maximum edge length allowed in each container
container_edges_allowed = [r * math.sqrt(2) for r in container_radii]

# Sort containers according to decreasing edge lengths allowed
container_edges_allowed, container_capacities = (
      map(list, zip(*sorted(zip(container_edges_allowed, container_capacities),
                            reverse=True))))

# Fill each container from widest to narrowest
packages_shipped = 0
package_idx = 0
container_idx = 0

while True:
    # Try to fit the largest package available
    if (package_edge_lengths[package_idx]
       < container_edges_allowed[container_idx]):
        # Package fits
        packages_shipped += 1

        # Reduce the container capacity
        container_capacities[container_idx] -= 1

        # Move to the next container if no room left in current
        # container
        if not container_capacities[container_idx]:
            container_idx += 1

        # If no containers left, print the result and exit
        if container_idx == num_containers:
            print(packages_shipped)
            sys.exit(0)

        # Now move onto the next package
        package_copies[package_idx] -= 1

        # Move to the next package type if no packages of current type
        # left
        if not package_copies[package_idx]:
            package_idx += 1

        # If no packages left, print the result and exit
        if package_idx == num_packages:
            print(packages_shipped)
            sys.exit(0)
    else:
        # Package did not fit! Move onto next package type
        package_idx += 1

        # If no packages left, print the result and exit
        if package_idx == num_packages:
            print(packages_shipped)
            sys.exit(0)
