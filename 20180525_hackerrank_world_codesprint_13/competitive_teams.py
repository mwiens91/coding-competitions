#!/usr/bin/env python3

import re
import sys


def task_1(dev1_, dev2_):
    """Execute task 1."""
    global developers

    if dev1_ == dev2_:
        pass
    elif not developers[dev1_] and not developers[dev2_]:
        # Form a team
        form_team(dev1_, dev2_)
    elif developers[dev1_] and developers[dev2_]:
        # Merge teams
        merge_teams(developers[dev1_], developers[dev2_])
    else:
        # Make developer without a team join a team
        if developers[dev1_]:
            join_team(dev2_, developers[dev1_])
        else:
            join_team(dev1_, developers[dev2_])


def task_2(c):
    """Execute task 2."""
    global teams_with_size, n
    sum_ = 0

    # Go through each team size (ts)
    for ts in range(n):
        for other_ts in range(ts + c, n):
            # Competitions within teams
            if other_ts == ts:
                sum_ += int(
                    teams_with_size[ts] * (teams_with_size[ts] - 1) / 2)

            if other_ts == n:
                # No more team sizes!
                break

            sum_ += teams_with_size[ts] * teams_with_size[other_ts]

    # Return result
    return sum_


def form_team(dev1, dev2):
    """Form a team."""
    global developers, teams, teams_with_size, size_for_team, next_team_counter

    # Assign the developers to the new team
    developers[dev1] = next_team_counter
    developers[dev2] = next_team_counter

    # Create the new team
    teams_with_size[1] += 1
    teams_with_size[0] -= 2

    size_for_team[next_team_counter] = 2
    teams[next_team_counter] = [dev1, dev2]

    # Increment the next team counter
    next_team_counter += 1


def join_team(dev, team):
    """Make a dev join a team."""
    global developers, teams, teams_with_size, size_for_team
    # Assign the developer to the team
    developers[dev] = team

    # Update the team
    old_team_size = size_for_team[team]
    teams[team].append(dev)
    update_team_size(team, old_team_size, old_team_size + 1)


def merge_teams(team1, team2):
    """Merge two teams."""
    global developers, teams, teams_with_size, size_for_team
    # Keep team1, and kill team2
    team1_size = size_for_team[team1]
    team2_size = size_for_team[team2]
    new_size = team1_size + team2_size

    # Move all devs on team2 to team1
    teams[team1] += teams[team2]

    for dev in teams[team2]:
        developers[dev] = team1

    # Update team1 and remove team2
    update_team_size(team1, team1_size, new_size)
    remove_team(team2, team2_size)


def update_team_size(team_, old_size, new_size):
    global teams, teams_with_size, size_for_team

    # Update the team size
    size_for_team[team_] = new_size
    teams_with_size[new_size - 1] += 1
    teams_with_size[old_size - 1] -= 1


def remove_team(team_, size_):
    global teams, teams_with_size, size_for_team

    # Remove the team
    del teams[team_]
    del size_for_team[team_]
    teams_with_size[size_ - 1] -= 1


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
n, _ = [int(x) for x in re.split(r'\D', lines[0])]
tasks = [[int(x) for x in re.split(r'\D', line)] for line in lines[1:]]

# A list of developers, 0-indexed, where each index represents the
# developer and the corresponding value represents their team
developers = [None] * n

# A dictionary of teams where the keys represent the teams and the
# values are a list of developers
teams = dict()

# A list of team sizes, where indicies represent sizes (minus 1) and the
# values are the number of teams of that size
teams_with_size = [0] * n
teams_with_size[0] = n      # All devs start teamless

# A dictionary of team sizes, where the keys represent the teams and the
# values represent their sizes
size_for_team = dict()

# A counter indicating the next team to create
next_team_counter = 1

# Go through each task
for task in tasks:
    # Determine task type and execute
    if task[0] == 1:
        # Zero index the devs
        task_1(task[1] - 1, task[2] - 1)
    else:
        print(task_2(task[1]))
