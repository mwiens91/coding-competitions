import sys
import re

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Separate names and height for each member
members = [[j for j in re.split("[^0-9a-zA-Z]", k)] for k in lines[1:]]
members = [[int(j[1]), j[0]] for j in members]

# Sort by height
members.sort(key=lambda x: x[1])
members.sort(key=lambda x: x[0])

# Now start printing by height
rootcount = 0
count = 0
startix = 1
stopix = 1
while count < len(members):
    # Print the name
    print(members[count][1], end=" ")
    count += 1;

    # Print more names of the same height
    while count < len(members) and members[count][0] == members[rootcount][0]:
        print(members[count][1], end=" ")
        count += 1
        stopix += 1

    # Print the ordering
    print(startix, end=" ")
    print(stopix)

    # Reset for next iteration
    startix = stopix + 1
    stopix = startix
    rootcount = count
