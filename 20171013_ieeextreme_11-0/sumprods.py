import sys
import re

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
lines = [lines[i] for i in range(len(lines)) if i % 2 == 0 and i != 0]
lines = [[int(i) for i in re.split("[^0-9]", j)] for j in lines]

for test in lines:
    if len(test) == 1:
        print(test[0])
        print(test[0])
        continue

    test.sort(reverse=True)

    numzeros = 0
    for num in test[::-1]:
        if num == 0:
            numzeros += 1
        else:
            break

    if numzeros:
        test = test[:-numzeros]

    newlist = [test[0]]

    for i in range(1, len(test)):
        fac = i % 2
        newlist = [test[i]]*(1 - fac) + newlist + [test[i]]*fac

    if newliststr > newliststr[::-1]:
        newlist = newlist[::-1]

    pivot = newlist[0]
    numpivots = 0
    for num in newlist[::-1]:
        if num == pivot:
            numpivots += 1
        else:
            break

    if numpivots:
        numpivots -= 1

    if numpivots:
        newlist = [pivot]*numpivots + newlist[:-numpivots]

    sum_ = 0
    for i in range(len(newlist) - 1):
        sum_ += newlist[i]*newlist[i+1]

    newlist = [0]*numzeros + newlist

    print(sum_)
    for i in range(len(newlist) - 1):
        print(newlist[i], end=" ")
    print(newlist[-1])
