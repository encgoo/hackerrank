#!/bin/python3

import os
import sys

#
# Complete the bricksGame function below.
#
def bricksGame(arr):
    # store at each position, (the best value to get, how many brick to take)
    best_choice = [(0, 0)] * len(arr)
    # initalize
    best_choice[-1] = (arr[-1], 1)
    best_choice[-2] = (arr[-1] + arr[-2], 2)
    best_choice[-3] = (arr[-1] + arr[-2] + arr[-3], 3)

    for i in range(len(arr) - 4, -1, -1):
        bricks_to_take = 1
        max_this_round = 0
        best_to_get_this_round = 0
        step_to_take_this_round = 0
        accum = 0
        while bricks_to_take <= 3:
            accum += arr[i + bricks_to_take - 1]
            best_to_get_this_round = accum
            other_player_start = i + bricks_to_take
            other_player_steps = best_choice[other_player_start][1]
            tmp = other_player_start + other_player_steps
            if tmp < len(arr):
                best_to_get_this_round += best_choice[tmp][0]

            if best_to_get_this_round > max_this_round:
                max_this_round = best_to_get_this_round
                step_to_take_this_round = bricks_to_take

            bricks_to_take += 1
        best_choice[i] = (max_this_round, step_to_take_this_round)

    #print(best_choice)

    return (best_choice[0][0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
