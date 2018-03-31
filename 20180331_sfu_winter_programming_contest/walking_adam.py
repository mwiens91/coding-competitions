#!/usr/bin/env python

from __future__ import division, print_function

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Go through each test case
for line in lines[1:]:
    idx = line.find('D')

    if idx == -1:
        print(len(line))
    else:
        print(idx)
