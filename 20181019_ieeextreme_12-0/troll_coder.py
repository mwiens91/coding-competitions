#!/usr/bin/env python3


# Troll IO
make_query = lambda x: int(input("Q " + " ".join([str(i) for i in x])))
make_answer = lambda x: print("A", *x)

# A troll!
N = int(input())

# Our answer and our ongoing query
correct_answer = []
query = [0] * N

# Initial query
num_zeros = make_query(query)
last_answer = num_zeros

# We'll take all N tries
for i in range(N - 1):
    query[i] = 1

    this_answer = make_query(query)

    if this_answer == last_answer + 1:
        correct_answer += [1]
    else:
        correct_answer += [0]

    last_answer = this_answer

# Find out if the last bit is a 0 or 1
if correct_answer.count(0) == num_zeros:
    correct_answer += [1]
else:
    correct_answer += [0]

# Give the troll the answer
make_answer(correct_answer)
