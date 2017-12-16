#/usr/bin/env python3

import re
import sys


TYPE1 = 1   # cats and elephants
TYPE2 = 2   # dogs and mice

class TripException(Exception):
    pass

def trip(xprime, transported, required, cargo):
    """Recursively try to transport animals.

    - xprime is the current animal number which is always less than x
    - transported is the number of animals that are included in cargo
    - required is the number of animals that need to be transported
    - cargo is an array specifying which animals are loaded at a given
      zoo number

    Uses animals, sources, and destins from outside the function.

    Simply returns if everything works out, otherwise raises a
    TripExcepetion
    """
    # Stopping condition
    if transported == required:
        return
    elif xprime == -1:
        raise TripException

    # Get source and destination for the animal just passed in
    thisanimal = animals[xprime]
    thissource = sources[xprime] - 1  # minus 1 so we can use it as an index
    thisdestin = destins[xprime] - 1

    # Determine if we're able to skip this animal
    abletoskip = xprime + 1 > required - transported

    # Determine the incompatible animal type
    notthisanimal = TYPE1 if thisanimal == TYPE2 else TYPE2

    # Try taking the animal
    try:
        newcargo = cargo[:]
        for l in range(thissource, thisdestin):
            if cargo[l] == notthisanimal:
                raise TripException
            else:
                newcargo[l] = thisanimal

        return trip(xprime - 1, transported + 1, required, newcargo)
    except TripException:
        # Try skipping the animal
        pass

    # Try skipping the animal
    if not abletoskip:
        raise TripException

    # This either works or throws an exception
    return trip(xprime - 1, transported, required, cargo)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the inputs
length = len(lines)
testcases = [lines[i:i+4] for i in range(1, length - 3, 4)]

# Run through each test case
for test in testcases:
    # Parse test case info
    _, n = [int(num) for num in re.split("\D", test[0])]
    animalsraw = [n for n in re.split("\s", test[1])]
    sourcesraw = [int(s) for s in re.split("\D", test[2])]
    destinsraw = [int(d) for d in re.split("\D", test[3])]

    # We'll delete some elements from these lists (possibly)
    animals = animalsraw[:]
    sources = sourcesraw[:]
    destins = destinsraw[:]

    # Remove any animals where source is greater than destination
    count = 0
    for x in enumerate(zip(sourcesraw, destinsraw)):
        if x[1][0] > x[1][1]:
            del animals[x[0] - count]
            del sources[x[0] - count]
            del destins[x[0] - count]
            count += 1

    # New number of effective animals
    nprime = n - count

    # Get out if we have no animals - I'm repeating code here but that's
    # okay for this purpose
    if not animals:
        resultstring = ""
        for x in range(n):
            resultstring += "-1 "

        print(resultstring.strip())
        continue


    # Name animals according to type 1 (cats and elephants) or type 2
    # (dogs and mice)
    animals = [TYPE1 if n == 'C' or n == 'E' else TYPE2 for n in animals]

    # Sort all lists in order of ascending destination
    z = zip(destins, sources, animals)
    destins, sources, animals = zip(*sorted(zip(destins, sources, animals)))

    # Now try to transport x+1 animals
    resultstring = ""
    failure = False
    for x in range(nprime):
        if failure:
            resultstring += "-1 "
            continue

        # 1 is a trivial case
        if x == 0:
            resultstring += "%d " % destins[0]
            continue

        # Now do every other case
        for i in range(x, nprime):
            try:
                trip(i, 0, x + 1, [0 for j in range(destins[i])])
                resultstring += "%d " % destins[i]
            except TripException:
                # If we still have more animals left, try those
                if i != n - 1:
                    # This is the *only* place we repeat for given x
                    continue

                # This and every subsequent trip is bad. Throw in '-1's
                failure = True
                resultstring += "-1 "
            break

    # Throw in '-1's for the animals we can't possibly transport
    for x in range(n - nprime):
        resultstring += "-1 "

    # Print results of test case
    print(resultstring.strip())
