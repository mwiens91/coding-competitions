"""A script to generate code to solve the two kings problem."""
#!/usr/bin/env python3

import re


# Generate starting positions
starting_positions = []

for i in range(5):
    for j in range(i, 5):
        starting_positions.append([i, j])

with open('generatedcode.py', 'a') as f:
    # Convenience function to write to file
    printf = lambda x: f.write(spaces + x + '\n')

    spaces = ''
    iteration = 1
    for pos in starting_positions:
        if iteration == 1:
            printf("if king1 == %s:" % pos)
        else:
            printf("elif king1 == %s:" % pos)

        iteration2 = 1
        for i in range(8):
            for j in range(8):
                spaces = ' ' * 4
                otherpos = [i, j]

                if otherpos == pos:
                    continue

                if iteration2 == 1:
                    printf("if king2 == %s:" % otherpos)
                else:
                    printf("elif king2 == %s:" % otherpos)

                print("King1: %s; King2: %s" % (pos, otherpos))
                q1 = input("Enter the row and column of the 1st Q:")
                q2 = input("Enter the row and column of the 2nd Q:")
                q3 = input("Enter the row and column of the 3rd Q:")

                q1 = re.split(r'\D', q1)
                q2 = re.split(r'\D', q2)

                if q3:
                    q3 = re.split(r'\D', q3)

                spaces = ' ' * 8

                if q3:
                    printf("'print(3)'")
                else:
                    printf("'print(2)'")

                printf("print('Q %s %s')" % (q1[0], q1[1]))
                printf("print('Q %s %s')" % (q2[0], q2[1]))

                if q3:
                    printf("print('Q %s %s')" % (q3[0], q3[1]))

                iteration2 += 1

        iteration += 1
