import sys
import re

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
letterset = [str(i) for i in lines[0]]
tests = [[str(i) for i in j] for j in lines[2:]]

for test in tests:
    printflag = False
    for i in range(len(test)):
        try:
            lscopy = letterset[:]
            testiter = test[i:]

            for char in testiter:
                    idx = lscopy.index(char)
                    lscopy = lscopy[idx+1:]

            print(len(test) - i)
            printflag = True
            break
        except ValueError:
            continue

    if not printflag:
        print(0)
