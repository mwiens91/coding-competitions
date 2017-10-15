import sys
import re

# Read input from stdin
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]

# Separate the test cases
numlines = len(lines)
testcases = [[lines[i],lines[i+1]] for i in range(numlines) if i % 2 == 1]

# Test each case
for case in testcases:
    loopflag = False

    vertices, edges = [int(i) for i in re.split("[^0-9]", case[0])]

    # Make sure we have connections
    if not edges:
        print(0)
        continue

    connectiondigits = re.split("[^0-9]", case[1])
    connections = [[int(connectiondigits[i]), int(connectiondigits[i+1])] for i in range(len(connectiondigits)) if i % 2 == 0]

    # Test for non-unique connections
    connections_set_list = [set(conn) for conn in connections]
    connections_set_set = set(frozenset(connset) for connset in connections)

    if len(connections_set_set) < len(connections_set_list):
        loopflag = True

    # Test for self-connection and isolated vertices
    if not loopflag:
        # Graph sets is a list containing lists representing graphs.
        # The lists contain the number of connections, and a set
        # containing the vertices in the graph.
        graphsets = []
        for connection in connections:
            a = connection[0]
            b = connection[1]

            # Test for self-loop
            if a == b:
                loopflag = True
                break

            # Put connection vertices in appropriate graph set.
            # Find out which graph a and b are in. Set the index to
            # False if not in any set. The indexes are incremented by
            # one to make conditions easier to test.
            placedflag = False
            aindex = False
            bindex = False
            for i in range(len(graphsets)):
                if a in graphsets[i][1]:
                    aindex = i + 1
                elif b in graphsets[i][1]:
                    bindex = i + 1

            if not (aindex or bindex):
                # Make a new graph
                graphsets += [[1,set([a,b])]]
            elif aindex and bindex:
                # Merge the graphs into a's graph
                graphsets[aindex-1][0] += 1 + graphsets[bindex-1][0]
                graphsets[aindex-1][1] = graphsets[aindex-1][1].union(graphsets[bindex-1][1])

                # Throw away b's graph
                del graphsets[bindex - 1]
            elif aindex and not bindex:
                # Add b to a's graph
                graphsets[aindex-1][0] += 1
                graphsets[aindex-1][1] = graphsets[aindex-1][1].union({b})
            else:
                # Add a to b's graph
                graphsets[bindex-1][0] += 1
                graphsets[bindex-1][1] = graphsets[bindex-1][1].union({a})

    # If N vertices in graph and >= N connections, then loop
    if not loopflag:
        for graph in graphsets:
            if len(graph[1]) <= graph[0]:
                loopflag = True
                break

    # Now print result
    print(1 * loopflag)
