#!/usr/bin/env python3
# coding: utf-8

import argparse
import re

# Get input path from command line
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)

args = parser.parse_args()

# Get input variables from text file
with open(args.input) as inputfile:
    lines = inputfile.readlines()

numLines = int(lines[0])

countattr = {"1", "2", "3"}
fillattr = {"E", "F", "S"}
colorattr = {"G", "P", "R"}
shapeattr = {"O", "D", "S"}

attrlist = [countattr, fillattr,colorattr,shapeattr]

for i in range(1, numLines + 1):
    cards = re.split("[^0-9A-Z]", lines[i].strip())
    card1 = cards[0]
    card2 = cards[1]
    card3 = ""

    for j in range(4):
        if card1[j] == card2[j]:
            card3 += card1[j]
        else:
            card3 += list(attrlist[j] - {card1[j], card2[j]})[0]

    print("Group %d: %s" % (i, card3))
