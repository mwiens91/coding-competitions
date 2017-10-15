#!/usr/bin/env python3
# coding: utf-8

import argparse
import re

# Get input path from command line
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)

args = parser.parse_args()

# Get input variables from text file
with open(args.input) as inputfile:
    lines = inputfile.readlines()

numMachinesStr = re.split("[^0-9]", lines[0])[0] # should agree with len(timesStr)
numLoadsStr = re.split("[^0-9]", lines[0])[1]
timesStr = re.split("[^0-9]", lines[1].strip()) # times as a string

numMachines = int(numMachinesStr)
timesInt = [int(x) for x in timesStr]

# Get latency
sortedtimesInt = timesInt[:]
sortedtimesInt.sort(reverse=True)
latency = sortedtimesInt[0]

# Start combining machines
newTimesList = []
i = 0

while i < numMachines:
    sum_ = timesInt[i]
    j = i + 1

    while True:
        if j < numMachines and sum_ + timesInt[j] <= latency:
            # We can combine
            sum_ += timesInt[j]
            j += 1
        else:
            # We can't combine - add combined machine to new time list
            newTimesList += [sum_]
            break

    i = j

print(len(newTimesList))
