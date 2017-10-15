import sys
import re

besttime = 10e8

def recursebook(currentbook, totaltime, topicsleft):
    global besttime
    totaltime += books[currentbook][0]

    if totaltime >= besttime:
        return

    topicsleft = topicsleft - books[currentbook][1]

    if not topicsleft:
        besttime = totaltime
        return

    for i in range(currentbook + 1, numbooks):
        recursebook(i, totaltime, topicsleft)

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Separate into books: each a list with time and topics
books = [[i for i in re.split("[^0-9a-zA-Z]", line)] for line in lines]
books = [[int(j[0]), frozenset(j[1:])] for j in books]

# Get total number of books
numbooks = len(books)

# Set of topics
topics = set()
for book in books:
    topics = topics.union(book[1])

# Start recursion
for i in range(numbooks):
    recursebook(i, 0, topics)

print(besttime)
