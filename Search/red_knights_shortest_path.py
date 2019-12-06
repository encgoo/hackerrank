#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


class Node:
    def __init__(self, parent, step):
        self.parent = parent
        self.step = step


def try_next(i, j, visited, step, q, n, i_end, j_end, parent_node):
    # see if we can make this step move
    if i < 0 or j < 0 or i >= n or j >= n:
        # out of bound. Don't do anything
        return None
    if visited[i][j]:
        # visited before
        return None

    node = Node(parent_node, step)
    if i == i_end and j == j_end:
        return node

    visited[i][j] = True
    q.append((i, j, node))
    return None


# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Find shortest path using Dijkstra algorithm
    visited = [[False] * n for _ in range(n)]
    root = Node(None, "")

    q = deque([(i_start, j_start, root)])
    end_node = None
    while len(q) > 0:
        sz = len(q)
        for i in range(sz):
            start = q.popleft()
            i = start[0]
            j = start[1]
            parent_node = start[2]
            # Now try all 6 possible moves
            # UL
            done = try_next(i - 2, j - 1, visited, "UL", q, n, i_end, j_end, parent_node)
            # UR
            done = done or try_next(i - 2, j + 1, visited, "UR", q, n, i_end, j_end, parent_node)
            # R
            done = done or try_next(i, j + 2, visited, "R", q, n, i_end, j_end, parent_node)
            # LR
            done = done or try_next(i + 2, j + 1, visited, "LR", q, n, i_end, j_end, parent_node)
            # LL
            done = done or try_next(i + 2, j - 1, visited, "LL", q, n, i_end, j_end, parent_node)
            # L
            done = done or try_next(i, j - 2, visited, "L", q, n, i_end, j_end, parent_node)

            if done:
                end_node = done
                break

        if done:
            break

    # Start from end_node reverse the path
    if end_node is None:
        print("Impossible")
        return
    out_list = []
    node = end_node
    while node.parent is not None:
        out_list = [node.step] + out_list
        node = node.parent
    print(len(out_list))
    print(" ".join(out_list))


if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
