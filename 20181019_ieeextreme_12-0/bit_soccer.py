#!/usr/bin/env python3

from bisect import bisect_left
import sys


def find_number_less_than_equal_to(a, num):
    pos = bisect_left(a, num)
    return pos


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
player_performance = [int(i) for i in lines[1].split()]
required_players = int(lines[2])
desired_performances = [[int(i) for i in line.split()] for line in lines[3:]]

# Let's be super greedy
player_performance.sort()

for perf in desired_performances:
    if bisect_left(player_performance, perf[0]) < required_players:
        print("NO")
    else:
        print("YES")
