#!/bin/python3

import math
import os
import random
import re
import sys


def count(n, pos, obs):
    if len(obs) == 0:
        return n - 1

    obs.sort()

    if pos > obs[-1]:
        return n - obs[-1] - 1
    elif pos < obs[0]:
        return obs[0] - 2
    else:
        index = 0
        while obs[index] < pos:
            index += 1

        return obs[index] - obs[index - 1] - 2


def count_col(n, c_q, r_q, obstacles):
    rows = [obs[0] for obs in obstacles if obs[1] == c_q]
    return count(n, r_q, rows)


def count_row(n, r_q, c_q, obstacles):
    # cols of all obs on the same row
    cols = [obs[1] for obs in obstacles if obs[0] == r_q]
    return count(n, c_q, cols)


def count_diagonal(n, r_q, c_q, obstacles):
    cn = 0
    # along x = y
    os1 = [obs for obs in obstacles if obs[0] - r_q == obs[1] - c_q]
    pos = [r_q + 1, c_q + 1]
    while pos[0] <= n and pos[1] <= n and pos not in os1:
        cn += 1
        pos[0] += 1
        pos[1] += 1
    pos = [r_q - 1, c_q - 1]
    while pos[0] > 0 and pos[1] > 0 and pos not in os1:
        cn += 1
        pos[0] -= 1
        pos[1] -= 1

    os2 = [obs for obs in obstacles if obs[0] + obs[1] == r_q + c_q]
    pos = [r_q + 1, c_q - 1]
    while pos[0] <= n and pos[1] > 0 and pos not in os2:
        cn += 1
        pos[0] += 1
        pos[1] -= 1
    pos = [r_q - 1, c_q + 1]
    while pos[0] > 0 and pos[1] <= n and pos not in os2:
        cn += 1
        pos[0] -= 1
        pos[1] += 1

    return cn


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    num = 0
    # count along the row
    num += count_row(n, r_q, c_q, obstacles)
    # count along the column
    num += count_col(n, c_q, r_q, obstacles)
    # count diagonally
    num += count_diagonal(n, r_q, c_q, obstacles)
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
