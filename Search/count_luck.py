#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countLuck function below.

h_count = 0


def find_path(matrix, loc, h, visited):
    global h_count
    i, j = loc
    # print("visiting {}".format(loc))
    if visited[i][j]:
        return
    visited[i][j] = True

    if matrix[i][j] == '*':
        # print("setting h {}".format(h))
        h_count = h
    # check 4 direction
    possible_ways = 0
    if i + 1 < len(matrix) and matrix[i + 1][j] != 'X':
        possible_ways += 1

    if j + 1 < len(matrix[0]) and matrix[i][j + 1] != 'X':
        possible_ways += 1

    if i - 1 >= 0 and matrix[i - 1][j] != 'X':
        possible_ways += 1

    if j - 1 >= 0 and matrix[i][j - 1] != 'X':
        possible_ways += 1

    h = h + 1 if (possible_ways > 1 and matrix[i][j] == 'M') or possible_ways > 2 else h
    # print("{}, {}, {}".format(loc, possible_ways, h))

    if i + 1 < len(matrix) and matrix[i + 1][j] != 'X':
        find_path(matrix, (i + 1, j), h, visited)

    if j + 1 < len(matrix[0]) and matrix[i][j + 1] != 'X':
        find_path(matrix, (i, j + 1), h, visited)

    if i - 1 >= 0 and matrix[i - 1][j] != 'X':
        find_path(matrix, (i - 1, j), h, visited)

    if j - 1 >= 0 and matrix[i][j - 1] != 'X':
        find_path(matrix, (i, j - 1), h, visited)


def countLuck(matrix, k):
    # recursive approach
    # first find M
    m_pos = (0, 0)
    visited = [[False] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'M':
                m_pos = (i, j)
                break
    h = 0
    find_path(matrix, m_pos, h, visited)

    if k == h_count:
        return "Impressed"
    else:
        # print(h_count)
        return "Oops!"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
