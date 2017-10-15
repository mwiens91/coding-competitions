import sys
import re

# Read input from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
numbers = [[int(a) for a in re.split("[^0-9]", b)] for b in lines]
n, m, k = numbers[0]
lions = numbers[1:]

for lion in lions:
    # Make the coordinates start at zero
    lion[0] -= 1
    lion[1] -= 1

# Increment the tiles where lions claim their teritory
board = [[0 for j in range(m)] for i in range(n)]
for lion in lions:
    y = lion[0]
    x = lion[1]
    d = lion[2]

    points = [(y + i, x + j) for i in range(-d,d+1) for j in range(-d,d+1) if
                y + i >= 0 and y + i <= n - 1 and
                x + j >= 0 and x + j <= m - 1 and
                abs(i) + abs(j) <= d]

    for (i,j) in points:
        board[i][j] += 1

# Now see which lion is sharing the most territory
bestlion = [0, 0]   # idx 0 is num terrs, idx 1 is lion number
for i in range(len(lions)):
    if board[lions[i][0]][lions[i][1]] - 1 > bestlion[0]:
        bestlion[0] = board[lions[i][0]][lions[i][1]] - 1
        bestlion[1] = i + 1

print(bestlion[1], bestlion[0])
