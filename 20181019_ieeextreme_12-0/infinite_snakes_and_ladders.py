#!/usr/bin/env python3

import math
import sys

POSITION = "position"
WINNER = "winner"
WON = "won"


def coordinate_to_position(x, y):
    global board_size

    if not y % 2:
        return 1 - x + board_size * y

    return x + board_size * (y - 1)


def position_to_coordinate(pos):
    global board_size

    y = math.ceil(pos / board_size)

    if not y % 2:
        x = 1 - pos + board_size * y
    else:
        x = board_size * (1 - y) + pos

    return (x, y)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
board_size = int(lines[0])
num_players = int(lines[1])
num_snakes = int(lines[2])
snake_positions_raw = [
    [int(i) for i in line.split()] for line in lines[3 : 3 + num_snakes]
]
num_ladders = int(lines[3 + num_snakes])
ladder_positions_raw = [
    [int(i) for i in line.split()]
    for line in lines[4 + num_snakes : 4 + num_snakes + num_ladders]
]
dice_rolls = [
    [int(x) for x in line.split()]
    for line in lines[5 + num_snakes + num_ladders :]
]
dice_rolls = [roll[0] + roll[1] for roll in dice_rolls]

# Make note of the last position
last_position = board_size ** 2 + 1

# Find the ladder and snake coordinates
snake_heads = []
snake_tails = []

for snake in snake_positions_raw:
    snake_heads += [coordinate_to_position(snake[0], snake[1])]
    snake_tails += [coordinate_to_position(snake[2], snake[3])]

ladder_starts = []
ladder_ends = []

for ladder in ladder_positions_raw:
    ladder_starts += [coordinate_to_position(ladder[0], ladder[1])]
    ladder_ends += [coordinate_to_position(ladder[2], ladder[3])]

# Keep track of players
players = {i: {WON: False, POSITION: 0} for i in range(1, num_players + 1)}

# Loop through players
current_player = 1

for roll in dice_rolls:
    # Use this to break out of the loop if all players have won
    game_over = False

    # Skip player if he's won already
    win_count = 0

    while True:
        if win_count == num_players:
            game_over = True
            break

        if players[current_player][WON]:
            current_player = current_player % num_players + 1
            win_count += 1
        else:
            break

    # Exit if all players have won
    if game_over:
        break

    # Move the player
    new_position = players[current_player][POSITION] + roll

    # Deal with final position, snakes, and ladders
    repeat = True

    while repeat:
        if new_position >= last_position:
            players[current_player][WON] = True
            new_position = last_position
            repeat = False
        elif new_position in snake_heads:
            snake_idx = snake_heads.index(new_position)
            new_position = snake_tails[snake_idx]
            repeat = True
        elif new_position in ladder_starts:
            ladder_idx = ladder_starts.index(new_position)
            new_position = ladder_ends[ladder_idx]
            repeat = True
        else:
            repeat = False

    players[current_player][POSITION] = new_position

    # Next player
    current_player = current_player % num_players + 1

for player_id, player in players.items():
    if player[WON]:
        print("%s %s" % (player_id, WINNER))
    else:
        print(
            "%s %s %s" % (player_id, *position_to_coordinate(player[POSITION]))
        )
