#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the prims function below.
def find_shortest_reachable(visited, shortest):
    min_dis = sys.maxsize
    ret_index = -1
    for index in range(len(shortest)):
        dis = shortest[index]
        if dis < min_dis and dis != -1 and visited[index] is False:
            ret_index = index
            min_dis = dis
    return ret_index

def prims(n, edges, start):
    # Use Prim algorithm
    visited = [False]*n
    shortest = [sys.maxsize]*n
    shortest[start - 1] = 0 # (distance to start, distance to tree)

    for s in range(n):
        node = find_shortest_reachable(visited, shortest)
        visited[node] = True
        es = [e for e in edges if e[0] == node + 1 or e[1] == node + 1]

        for e in es:
            node_tmp = (e[0] if e[1] == node + 1 else e[1]) - 1
            if visited[node_tmp] is False:
                shortest[node_tmp] = min(shortest[node_tmp], e[2])

    ret = 0
    for s in shortest:
        ret += s

    return ret



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
