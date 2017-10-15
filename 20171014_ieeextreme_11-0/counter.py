import sys
import re

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]
lines = [[int(j) for j in re.split("[^0-9]", k)] for k in lines]

# Parse the input
a = lines[1]
q = lines[2]
lrs = lines[3:]

# Evaluate cost of each subarray
for lr in lrs:
    l = lr[0] - 1
    r = lr[1]

    cost = 0

    alr = list(a[l:r])
    blr = list(alr)

    # Deal with degenerate cases
    if len(alr) == 1:
        print(0)
        continue
    elif len(alr) == 2:
        if alr[1] > alr[0]:
            print(2)
        else:
            print(0)

        continue

    # Generate new Falr
    for i in range(len(blr) - 2, -1, - 1):
        if blr[i] < blr[i+1]:
            for j in range(len(blr) - 1, i, -1):
                if blr[j] > blr[i]:
                    blr[i], blr[j] = blr[j], blr[i]
                    temp = blr[i+1:]
                    temp.sort()
                    blr = blr[:i+1] + temp
                    break

            break

    for i,j in zip(alr,blr):
        if i != j:
            cost += 1

    print(cost)
