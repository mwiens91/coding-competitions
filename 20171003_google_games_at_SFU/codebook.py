import re

##########################READ BOOK ###########################################
chapterfiles = ["chpt0" + str(i) + ".txt" for i in range(1,10)] + ["chpt10.txt"]
chapters = ["" for i in range(1,11)]

for i in range(10):
    with open(chapterfiles[i]) as inputfile:
        chapters[i] = inputfile.readlines()

chapters = [[i.strip() for i in j] for j in chapters]
fullchapters = [" ".join(i) for i in chapters]

chapterwords = [re.split(" ", i) for i in fullchapters]
chapterwords = [[i for i in j if i != ""] for j in chapterwords]
##############################################################################

#### READ INPUT ####
with open("input.txt") as inputfile:
    indicesstr = inputfile.readlines()

indices = [[int(j) for j in re.split("[^0-9]", i) if j != ""] for i in indicesstr]

for index in indices:
    print(chapterwords[index[0] - 1][index[1] - 1][index[2] - 1], end="")
