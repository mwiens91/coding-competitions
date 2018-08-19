#!/usr/bin/env python3

import copy
import sys


def do_event_one(t, pt, si, sj):
    global prediction_sets_by_stock
    global prediction_sets_by_group

    # Get the old prediction sets
    prediction_set_by_stock = copy.deepcopy(prediction_sets_by_stock[pt])
    prediction_set_by_group = copy.deepcopy(prediction_sets_by_group[pt])

    # Already positively correlated. Do nothing.
    if prediction_set_by_stock[si] == prediction_set_by_stock[sj]:
        prediction_sets_by_stock[t] = prediction_set_by_stock
        prediction_sets_by_group[t] = prediction_set_by_group

        return

    # Combine the groups
    group_to_add_to = prediction_set_by_stock[si]
    group_to_remove = prediction_set_by_stock[sj]

    # Move all stocks from one group into the other
    for s in prediction_set_by_group[group_to_remove]:
        prediction_set_by_stock[s] = group_to_add_to

    prediction_set_by_group[group_to_add_to] = (
        prediction_set_by_group[group_to_add_to]
        | prediction_set_by_group[group_to_remove])

    # Remove the empty group
    del prediction_set_by_group[group_to_remove]

    # Save the prediction set
    prediction_sets_by_stock[t] = prediction_set_by_stock
    prediction_sets_by_group[t] = prediction_set_by_group


def do_event_two(pt, *s):
    global prediction_sets_by_stock

    # Count the number of unique groups we have
    groups_list = []

    for stock in s:
        groups_list.append(prediction_sets_by_stock[pt][stock])

    unique_groups = len(set(groups_list))

    print(pow(2, unique_groups, int(1e9 + 7)))


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_stocks, _ = [int(i) for i in lines[0].split()]
queries = [[int(i) for i in line.split()] for line in lines[1:]]

# Record some information
prediction_sets_by_stock = {0: {i: i for i in range(1, num_stocks + 1)}}
prediction_sets_by_group = {0: {i: set((i,)) for i in range(1, num_stocks + 1)}}

for event_number, query in enumerate(queries, 1):
    if query[0] == 1:
        do_event_one(event_number, *query[1:])
    else:
        do_event_two(*query[1:])
