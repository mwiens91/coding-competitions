#!/usr/bin/env python3

from statistics import mean, median
import sys


def running_time(x):
    global all_prices

    return sum([abs(p-x) for p in all_prices])


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_stocks = int(lines[0])

stocks = [[int(i) for i in lines[j].split()]
          for j in range(2, num_stocks * 2 + 1, 2)]

# Calculate the means
means = [mean(stock) for stock in stocks]

# Flatten the stocks and get a list of all prices
all_prices = [price for stock in stocks for price in stock]

# Now take the median of all stock prices (call this the "meta mean") -
# this is our ideal mean
meta_mean = median(all_prices)

# Find the best existing mean
best_mean = min(means, key=lambda x: abs(x - meta_mean))

# Print the answer
print(running_time(best_mean))
