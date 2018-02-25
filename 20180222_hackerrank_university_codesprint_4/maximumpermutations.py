#!/usr/bin/env python3

import collections
import sys


# Number of letters in the English alphabet
LETTERS = 26

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Gather scenarios
num_scenarios = int(lines[0])
scenarios = [lines[1+2*i:3+2*i] for i in range(num_scenarios)]

# Function to convert character to number
char_to_number = lambda x: ord(x) - ord('a')

# Solve each scenario
for scenario in scenarios:
    # Get the source of permutations and string to match
    word = list(scenario[0])
    matchstring = list(scenario[1])

    # Make sure the set of letters in word is a subset of the letters in
    # the matching string
    if not set(word) <= set(matchstring):
        print(-1)
        continue

    # Get the frequencies of the letters in the word
    wordfreq = [0] * LETTERS
    for char in word:
        wordfreq[char_to_number(char)] += 1

    # Get the length of the word and matching string
    wordlen = len(word)
    matchlen = len(matchstring)

    # Deal with the case where the word is longer than the matching
    # string
    if wordlen > matchlen:
        print(-1)
        continue

    # Now maintain a queue that goes through the letters of the matching
    # string in chunks the size of the word length. If the chunk
    # contains a valid permutation then increment its frequency in a
    # separate tracker.
    permutation_count = dict()
    nextidx = wordlen

    # Get the first chunk
    match_chunk = collections.deque(matchstring[:nextidx])

    # Track the letters in the first chunk
    chunkfreq = [0] * LETTERS
    for char in match_chunk:
        chunkfreq[char_to_number(char)] += 1

    # Now go through the chunks
    while True:
        # Check if this is a valid permutation and record it if so
        if chunkfreq == wordfreq:
            thispermutation = ''.join(match_chunk)

            if thispermutation in permutation_count:
                permutation_count[thispermutation] += 1
            else:
                permutation_count[thispermutation] = 1

        # Continue until we've gone through the whole match string
        if nextidx == matchlen:
            break

        # Move to the next chunk. Remove the left letter.
        char_removed = match_chunk.popleft()
        chunkfreq[char_to_number(char_removed)] -= 1

        # Add the right letter
        char_next = matchstring[nextidx]
        chunkfreq[char_to_number(char_next)] += 1
        match_chunk.append(char_next)

        nextidx += 1

    # Print the highest occuring permutation. If there is a tie, take
    # the permutation that is lexicographically lowest.
    if not permutation_count:
        print(-1)
    else:
        # Sort lexicographically first, then sort that list for a
        # maximum. Keep in mind that Python's sort is stable.
        print(sorted(sorted(permutation_count),
                     key=(lambda key: permutation_count[key]),
                     reverse=True)[0])
