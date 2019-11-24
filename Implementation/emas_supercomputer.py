#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoPluses function below.
def check_overlapping(p1, p2):
    # check if two pluses overlap with each other
    if p1[0] == p2[0]:
        return (p1[2] + p2[2]) > abs(p1[1] - p2[1]) - 1

    if p1[1] == p2[1]:
        return (p1[2] + p2[2]) > abs(p1[0] - p2[0]) - 1

    diff_i = abs(p1[0] - p2[0])
    diff_j = abs(p1[1] - p2[1])

    no_overlapping = (p1[2] < diff_i or p2[2] < diff_j) and (p2[2] < diff_i or p1[2] < diff_j)
    return not no_overlapping


def findPlus(grid, i, j):
    sz = 0
    while i - sz >= 0 and i + sz < len(grid) and j - sz >= 0 and j + sz < len(grid[0]) and grid[i - sz][j] == 'G' and \
            grid[i + sz][j] == 'G' and grid[i][j - sz] == 'G' and grid[i][j + sz] == 'G':
        sz += 1

    return sz - 1


def twoPluses(grid):
    all_pluses = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'G':
                sz = findPlus(grid, i, j)
                all_pluses.append((i, j, sz))
    ret_max = 0
    # go though any two pluses
    for i in range(len(all_pluses)):
        for j in range(i + 1, len(all_pluses)):
            if check_overlapping(all_pluses[i], all_pluses[j]) is False:
                # non-overlaping pluses. Just multiply
                pr = (all_pluses[i][2] * 4 + 1) * (all_pluses[j][2] * 4 + 1)
                ret_max = max(ret_max, pr)
            else:
                # overlaping
                diff_i = abs(all_pluses[i][0] - all_pluses[j][0])
                diff_j = abs(all_pluses[i][1] - all_pluses[j][1])
                if diff_i * diff_j != 0:
                    # two pluses have centers aligned
                    # There are three cases here
                    # 1. Taking all_pluses[i][2]
                    sz1 = all_pluses[i][2]
                    max_diff = max(diff_i, diff_j)
                    if sz1 >= max_diff:
                        sz2 = min(diff_i, diff_j) - 1
                    else:
                        sz2 = min(all_pluses[j][2], max_diff - 1)
                    pr1 = (sz1 * 4 + 1) * (sz2 * 4 + 1)
                    # 2. Taking all_pluses[1][2]
                    sz1 = all_pluses[j][2]
                    max_diff = max(diff_i, diff_j)
                    if sz1 >= max_diff:
                        sz2 = min(diff_i, diff_j) - 1
                    else:
                        sz2 = min(all_pluses[i][2], max_diff - 1)
                    pr2 = (sz1 * 4 + 1) * (sz2 * 4 + 1)
                    pr = max(pr1, pr2)
                    # there is a close rectangle
                    if all_pluses[i][2] >= max_diff and all_pluses[j][2] >= max_diff:
                        min_diff = min(diff_i, diff_j)
                        pr3 = (min_diff * 4 + 1) ** 2
                        pr = max(pr, pr3)
                    ret_max = max(ret_max, pr)
                else:
                    # not aligned.
                    diff = max(diff_i, diff_j) - 1
                    min_sz = min(all_pluses[i][2], all_pluses[j][2])
                    if min_sz < diff // 2:
                        sz1 = min_sz
                        sz2 = diff - sz1
                    else:
                        sz1 = int(diff / 2)
                        sz2 = diff - sz1
                    pr = (sz1 * 4 + 1) * (sz2 * 4 + 1)
                    ret_max = max(ret_max, pr)
    return ret_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
