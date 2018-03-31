#!/usr/bin/env python

from __future__ import division, print_function

import re
import sys


def sqrt_floor(n):
    """Babylonian Method"""
    low = n // 2
    high = 2

    while abs(high - low) > 1:
        high = (low + ) // 2
        low = n // high

    return low


def query1(L, R):
    global array

    for idx in range(L, R + 1):
        array[idx] = sqrt_floor(array[idx])


def query2(L, R):
    global array

    sum_ = 0

    for idx in range(L, R + 1):
        sum_ += array[idx]

    print(sum_)


def query3(L, R, x):
    global array

    # Compensate for minus 1 while parsing input
    x += 1

    for idx in range(L, R + 1):
        array[idx] += x


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input - queries are 0-indexed
array = [int(x) for x in re.split(r' ', lines[2])]
queries = [[int(x) - 1 for x in re.split(r'\D', line)] for line in lines[3:]]

# Group the query functions
query_funcs = [query1, query2, query3]

# Go through the queries
for query in queries:
    query_funcs[query[0]](*query[1:])
