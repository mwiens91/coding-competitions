#!/usr/bin/env python3

import sys

NO_SOLUTION = "impossible"
USED_BRACKET = "X"


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Get some free points for now
brackets = list(lines[0])
num_brackets = len(brackets)
sequence_one_desired_length = num_brackets // 2

# Check if possible
if (
    sequence_one_desired_length % 2
    or brackets.count("(") != brackets.count(")")
    or brackets.count("[") != brackets.count("]")
):
    print(NO_SOLUTION)
    sys.exit(0)

# Greedy algorithm
solution = [2] * num_brackets
sequence_one_length = 0

while sequence_one_length < sequence_one_desired_length:
    # Find first index that isn't a 2
    starting_bracket_idx = solution.index(2)

    # Find the type of this index and sanity check
    opening_bracket = brackets[starting_bracket_idx]

    # Sanity check
    if opening_bracket in (")", "]"):
        print(NO_SOLUTION)
        sys.exit(0)

    # Find the matching closing brace and put it in sequence one
    closing_bracket = ")" if opening_bracket == "(" else "]"
    closing_bracket_idx = brackets.index(closing_bracket)

    solution[starting_bracket_idx] = 1
    solution[closing_bracket_idx] = 1
    sequence_one_length += 2

    # Mark the brackets we just used as used
    brackets[starting_bracket_idx] = USED_BRACKET
    brackets[closing_bracket_idx] = USED_BRACKET

print(*solution)
