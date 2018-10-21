#!/usr/bin/env python3


# Troll IO
make_query = lambda x: int(input("Q " + " ".join([str(i) for i in x])))
make_answer = lambda x: print("A", *x)

# Go through each test case
num_test_cases = int(input())

for _ in range(num_test_cases):
    # A troll!
    N = int(input())

    # Our answer and our ongoing query
    query = [0] * N

    # Initial query
    num_zeros = make_query(query)
    last_answer = num_zeros

    # Query repeatedly
    idx = 0

    while True:
        # Exit if we've guessed it right already
        if last_answer == N:
            break

        # Change the next two to ones
        query[idx] = 1
        query[idx + 1] = 1

        this_answer = make_query(query)

        if this_answer == last_answer + 2:
            # Yay!
            last_answer += 2
        elif this_answer == last_answer - 2:
            # Completely wrong
            query[idx] = 0
            query[idx + 1] = 0
        else:
            # Partially right
            query[idx + 1] = 0

            this_other_answer = make_query(query)

            if this_other_answer == last_answer + 1:
                # Now it's right
                pass
            else:
                # Okay, let's fix it
                query[idx] = 0
                query[idx + 1] = 1

            last_answer += 1

        idx += 2

    # Give the troll the answer
    make_answer(query)
