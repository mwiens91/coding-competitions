import sys
import re
from math import floor, sqrt

def recurseme(lodgesfree, familynum, hotelcount):
    global minhotels
    if hotelcount >= minhotels:
        return

    if familynum == n:
        minhotels = hotelcount
        return

    if not options[familynum]:
        # No options
        recurseme(lodgesfree, familynum + 1, hotelcount + 1)
    else:
        for option in options[familynum]:
            optionset = set([option])
            recurseme(lodgesfree - optionset, familynum + 1, hotelcount + 1 - 1 * bool(lodgesfree & optionset))


# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse data
n = int(lines[0])
visits = [[int(i) for i in re.split("[^0-9]", j)] for j in lines[1:]]

# Set up variables
familyset = set(range(n))
options = [frozenset(familyset - (set(visits[i]) | set([i]))) for i in range(n)]
options.sort
minhotels = n

recurseme(familyset, 0, 0)
print(minhotels)
