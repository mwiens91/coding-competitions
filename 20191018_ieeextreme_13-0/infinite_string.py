#!/usr/bin/env python3

import math
import sys

EPSILON = 0.001


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
cases = [[int(x) for x in line.split()] for line in lines[1:]]

# Solve each test case
for case in cases:
    k, x = case

    # Use one-indexing for x
    x += 1

    # First determine which word length group s the character at x
    # corresponds to
    s = 1

    total_characters_including_s = k
    total_characters_excluding_s = 0

    while total_characters_including_s < x:
        s += 1

        total_characters_excluding_s = total_characters_including_s
        total_characters_including_s += s * k ** s

    # Determine the position xs of the character x within the group s
    xs = x - total_characters_excluding_s

    # Determine the position xss of the character x within its word in
    # group s
    xss = xs - s * math.floor((xs - 1) / s)

    # Determine the character which corresponds to x
    letter_in_word = 1

    # Determine the letter for each position in the word until we reach
    # the target position
    while letter_in_word < xss:
        # Determine the letter (zero-indexed) corresponding to the
        # position of the letter we're interested in
        c = s * k ** (s - letter_in_word)
        m = math.floor(xs / c - EPSILON)

        # We redefine xs to be the position in the group s starting at
        # words that start at the letter corresponding to m
        xs -= c * m

        letter_in_word += 1

    m = math.floor(xs / (s * k ** (s - letter_in_word)) - EPSILON)

    # Map number to character
    print(chr(ord("`") + m + 1))
