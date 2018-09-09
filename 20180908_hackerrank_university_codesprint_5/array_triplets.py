#!/usr/bin/env python3

import sys


def add_or_not(running_total,
               triplet_indices,
               current_idx,
               array,
               target_total,
               final_idx):
    """Recursive function for the program."""
    global triplets

    # Stop if we're done
    if current_idx > final_idx:
        return

    # Try skipping the number
    add_or_not(
        running_total,
        triplet_indices[:],
        current_idx + 1,
        array,
        target_total,
        final_idx)

    # Try adding the number
    running_total += array[current_idx]
    triplet_indices += [current_idx]

    #if running_total == target_total and triplet_indices:
    if running_total == target_total:
        triplets.append(triplet_indices[:])

    add_or_not(
        running_total,
        triplet_indices,
        current_idx + 1,
        array,
        target_total,
        final_idx)


def add_or_not_subarray(
        running_total,
        current_idx,
        indices_added,
        array,
        target_total,
        final_idx):
    """Recursive function for the program."""
    global triplet_count

    # Stop if we're done
    if current_idx > final_idx:
        return

    # Try skipping the number
    add_or_not_subarray(
        running_total,
        current_idx + 1,
        indices_added,
        array,
        target_total,
        final_idx)

    # Try adding the number
    running_total += array[current_idx]
    indices_added += 1

    if running_total == target_total and indices_added != final_idx + 1:
        triplet_count += 1

    add_or_not_subarray(
        running_total,
        current_idx + 1,
        indices_added,
        array,
        target_total,
        final_idx)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
array_length = int(lines[0])
array = [int(i) for i in lines[1].split()]

# Find sum of array and sum for each subarray
array_sum = sum(array)
subarray_sum = array_sum / 3

# Handle trivial cases
if subarray_sum != int(subarray_sum):
    # Not possible to divide into triplets!
    print(0)
    sys.exit(0)

# Find all triplets
triplets = []
triplet_count = 0

add_or_not(0, [], 0, array, subarray_sum, array_length - 1)

for triplet in triplets:
    subarray = array[:]

    for idx in sorted(triplet, reverse=True):
        del subarray[idx]

    add_or_not_subarray(0, 0, 0, subarray, subarray_sum, len(subarray) - 1)

print(triplet_count)
