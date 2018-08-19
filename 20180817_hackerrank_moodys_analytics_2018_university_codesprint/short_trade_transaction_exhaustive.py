#!/usr/bin/env python3
"""Brute force all possible answers."""

import pickle

def solve_answer(a, m):
    count = 0

    def recurse_me(a, m, remaining):
        nonlocal count
        if not remaining:
            count += 1

        if not m:
            return

        for i in range(1, min(a, remaining) + 1):
            recurse_me(i - 1, m - 1, remaining - i)

    recurse_me(a, m, a)

    return count



# Store answers here
# answer_dict = {(a, m): solve_answer(a, m)
#                for a in range(1, 101) for m in range(1, 101)}
answer_dict = {}
iteration = 0

for a in range(1, 101):
    for m in range(1, 101):
        iteration += 1
        print("Performing iteration %d" % iteration)

        answer_dict[(a, m)] = solve_answer(a, m)


with open('answers.pickle', 'wb') as f:
    pickle.dump(answer_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
