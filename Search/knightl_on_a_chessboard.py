#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the knightlOnAChessboard function below.
def try_next(i, j, visited, q, n):
    if i == n - 1 and j == n - 1:
        return True
    # check if outbounded
    if i < 0 or j < 0 or i >= n or j >= n:
        # don't do anything
        return False
    if visited[i][j]:
        return False

    visited[i][j] = True
    q.append((i, j))
    return False


def get_count(i, j):
    ret = -1
    # Use Dijkstra algorithm.
    visited = [[False] * n for _ in range(n)]
    step_count = -1
    # put (0,0) into the deque
    q = deque([(0, 0)])
    done = False
    while len(q) > 0:
        sz = len(q)
        step_count += 1
        for _ in range(sz):
            start = q.popleft()
            visited[start[0]][start[1]] = True
            # try all 8 different moves
            # +i, +j
            done = try_next(start[0] + i, start[1] + j, visited, q, n)
            # +i, -j
            done = done or try_next(start[0] + i, start[1] - j, visited, q, n)
            # -i, + j
            done = done or try_next(start[0] - i, start[1] + j, visited, q, n)
            # -i, -j
            done = done or try_next(start[0] - i, start[1] - j, visited, q, n)
            # +j, +i
            done = done or try_next(start[0] + j, start[1] + i, visited, q, n)
            # +j, -i
            done = done or try_next(start[0] + j, start[1] - i, visited, q, n)
            # -j, + i
            done = done or try_next(start[0] - j, start[1] + i, visited, q, n)
            # -j, -i
            done = done or try_next(start[0] - j, start[1] - i, visited, q, n)

            if done:
                break

        if done:
            break

    ret = step_count + 1 if done else -1
    return ret


def knightlOnAChessboard(n):
    counts = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(1, n):
        for j in range(1, i):
            counts[i - 1][j - 1] = counts[j - 1][i - 1]

        for j in range(i, n):
            counts[i - 1][j - 1] = get_count(i, j)

    return counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
