#!/usr/bin/env python3

import re
import sys


def is_group_valid(group_):
    """Tests if a group is valid."""
    global b, f, s, t

    # Test group against constraints
    for val_, constraint in zip(group_, [b, f, s, t]):
        if val_ > constraint:
            # Invalid
            return False

    # Valid
    return True


def can_students_join_group(joined, joiner):
    """Test if joiner can join joined's group."""
    global students, groups

    # Make the hypothetical group
    test_group = groups[students[joined]['group']][:]
    test_group[0] += 1
    test_group[students[joiner]['grade']] += 1

    # Return its validity
    if is_group_valid(test_group):
        return True
    return False


def can_students_merge_group(student_1, student_2):
    """Test if students can merge their group.

    Merging is symmetric in that the order of the students passed in
    doesn't change the result.
    """
    global students, groups

    # Gather the groups to join
    group1 = groups[students[student_1]['group']][:]
    group2 = groups[students[student_2]['group']][:]

    # Make the hypothetical group
    test_group = [x + y for x, y in zip(group1, group2)]

    # Return its validity
    if is_group_valid(test_group):
        return True
    return False


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input

# n - total number of students
# a and b - minimum and maximum number of students in a group,
#   respectively
# f, s, and t - maximum number of first, second and third grade students
#   in a group, respectively
n, _, a, b, f, s, t = [int(x) for x in re.split(r'\D', lines[0])]

# Make sure that b >= a. If not then get out.
if a > b:
    print("no groups")

# Keys are students' names. Values are a dict containing the grade they
# are in, and the group they are in.
students = dict()

for line in lines[1:n+1]:
    # Add student to student dictionary
    name, grade = re.split(r' ', line)
    students[name] = {'grade': int(grade), 'group': None}

# Parse the requests
requests = [[name for name in re.split(r' ', line)] for line in lines[n+1:]]

# A dictionary of groups, each group is a list containing, in this order,
# - the total number of students in the group
# - the number of first grade students in the group
# - the number of second grade students in the group
# - the number of third grade students in the group
# Also, groups are labelled 1, 2, 3, 4, etc.
groups = dict()

# Group memberships is a dict of lists containing the names of the
# students in each group
group_memberships = dict()

# A counter for the label of the next group
next_group = 1

# Now fulfill each request
for request in requests:
    # Get the students
    student1, student2 = request

    # Make sure the students are different
    if student1 == student2:
        continue

    # Three cases:
    # (1) Neither student is in a group. They form a new group if
    #   possible.
    # (2) One of the students in a group. The other student joins that
    #   group if possible.
    # (3) Both students are already in a group. If they are already in
    #   the same group, there is nothing left to do. If they are in
    #   different groups, merge the groups if possible.

    # Test (1) first, then (3), and then (2)
    if not (students[student1]['group'] or students[student2]['group']):
        # Case (1): form the group. Constraints guarantee this is
        # possible always
        students[student1]['group'] = next_group
        students[student2]['group'] = next_group
        groups[next_group] = [2, 0, 0, 0]
        groups[next_group][students[student1]['grade']] += 1
        groups[next_group][students[student2]['grade']] += 1
        group_memberships[next_group] = [student1, student2]

        # Increment the next_group counter
        next_group += 1
    elif students[student1]['group'] and students[student2]['group']:
        # Case (3): try and merge group if they are not already in the
        # same group
        if (students[student1]['group'] != students[student2]['group']
               and can_students_merge_group(student1, student2)):
            # Merge the groups, doesn't matter which, so keep student1's
            # group
            static_group = students[student1]['group']
            joining_student = student2
            joining_group = students[student2]['group']

            # Merge the groups
            for student in group_memberships[joining_group]:
                students[student]['group'] = static_group

            for idx, val in enumerate(groups[joining_group]):
                groups[static_group][idx] += val

            group_memberships[static_group] += (
                group_memberships[joining_group])

            # Kill the old group
            del groups[joining_group]
            del group_memberships[joining_group]
    else:
        # Case (2): test if lone student can join group
        lone_student = student1 if students[student2]['group'] else student2
        member_student = student1 if lone_student is student2 else student2

        if can_students_join_group(member_student, lone_student):
            # Add the lone student to the group
            group_to_join = students[member_student]['group']
            students[lone_student]['group'] = group_to_join
            groups[group_to_join][0] += 1
            groups[group_to_join][students[lone_student]['grade']] += 1
            group_memberships[group_to_join].append(lone_student)

# Now find the largest group(s) that meet the minimum group threshold
num_largest_students = a
largest_student_groups = []

for group_id, group in groups.items():
    num_students = group[0]
    if num_students == num_largest_students:
        # Tied
        largest_student_groups.append(group_id)
    if num_students > num_largest_students:
        # Winner
        num_largest_students = num_students
        largest_student_groups = [group_id]

# Collect the students in the largest groups
winning_students = []

for group_id in largest_student_groups:
    winning_students += group_memberships[group_id]

# Print the answer
if winning_students:
    for student in sorted(winning_students):
        print(student)
else:
    print("no groups")
