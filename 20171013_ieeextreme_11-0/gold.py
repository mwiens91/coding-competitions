import sys
import re

mindistance = 100000
bestpaths = []

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def recursepath(blacklist, pathlist, distance, nowidx):
    global mindistance
    global bestpaths

    pathlist += [nowidx]

    # If too much distance
    if distance > mindistance:
        return

    if nowidx == stop:
        if mindistance == distance:
            bestpaths += [pathlist]
        else:
            bestpaths = [pathlist]
            mindistance = distance

    # Try and go somewhere
    nodeidxs = [i for i in range(len(connections)) if nowidx in connections[i][0] and i not in blacklist]
    for node in nodeidxs:
        # Take this path
        recursepath(blacklist[:] + [node], pathlist[:], distance + connections[node][1], list(connections[node][0] - set([nowidx]))[0])


# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]
numbers = [[int(i) for i in re.split("[^0-9]", j)] for j in lines]

# Find starting and stopping ids
goldvals = [i for i in numbers if len(i) == 1]
goldvals.sort()
start = goldvals[0][0]
stop = goldvals[-1][0]

# Build list of connections: a list of lists: first element containing
# set of vertices, second element containing integer distance
connections = [i for i in numbers if len(i) == 3]
connections = [[frozenset(i[:2]), i[2]] for i in connections]

# Start recursion
recursepath([], [], 0, start)

# Get dat gold
itersum = 0
maxgold = 0
for bestpath in bestpaths:
    for id_ in bestpath:
        prod = 1
        iter_ = 0

        for prime in gen_primes():
            prod *= prime

            if prod > id_:
                break

            iter_ += 1

        itersum += iter_
    if itersum > maxgold:
        maxgold = itersum

print(maxgold)
