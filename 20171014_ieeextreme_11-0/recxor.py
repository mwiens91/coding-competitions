import sys
import re
from math import floor

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the testcases
testcases = [[int(i) for i in re.split("[^0-9]", j)] for j in lines[1:]]

# Credit goes to v78 on StackExchange for the algorithm
def f(a):
     res = [a, 1, a+1, 0]
     return res[a%4]

def getXor(a, b):
     return f(b) ^ f(a-1)

# Iterate through test-cases
for test in testcases:
    l, h, n, d1, d2 = test

    i1 = floor((d1-n)/l)
    i2 = floor((d2-n)/l)

    j1 = d1 - n - l*i1
    j2 = d2 - n - l*i2

    if j1 > j2:
        temp = j2
        j2 = j1
        j1 = temp

    xorprod = 0

    for i in range(h):
        if i < i1 or i > i2:
            xorprod ^= getXor(n + i*l, n + (i+1)*l - 1)
        else:
            xorprod ^= getXor(n + i*l, n + i*l + j1 - 1)
            xorprod ^= getXor(n + i*l + j2 + 1, n + (i+1)*l - 1)

    print(xorprod)
