import sys
import re

# credit to https://stackoverflow.com/questions/38445069/fast-fibonacci-computation
def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]
gens = [int(i) for i in lines[1:]]

for gen in gens:
    gen %= 60
    print(fib(gen + 1) % 10)
