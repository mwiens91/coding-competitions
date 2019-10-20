#!/usr/bin/env python3

MATCH = "MATCH"


# Get N from input
n = int(input())

# Look at all cards
card_map = {}

for i in range(n):
    idx = 2 * (i + 1) - 1

    response = input("%s %s" % (idx, idx + 1))

    if response == MATCH:
        continue

    val1, val2 = response.split()

    if val1 not in card_map:
        card_map[val1] = [idx]
    else:
        card_map[val1] += [idx]

    if val2 not in card_map:
        card_map[val2] = [idx + 1]
    else:
        card_map[val2] += [idx + 1]

# Get remaining matches
for _, idxs in card_map.items():
    input("%s %s" % (idxs[0], idxs[1]))

print(-1)
