#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the bfs function below.
def bfs(n, m, edges, s):
    dis = [-1] * n
    dis[s - 1] = 0
    q = deque([s])
    distance = 0
    # optimize the access of edges
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0] - 1].append(e[1])
        g[e[1] - 1].append(e[0])

    while len(q) > 0:
        # print(q)
        sz = len(q)
        distance += 6
        # print("{}, {}, {}".format(distance, q, dis))
        for i in range(sz):
            node = q.popleft()
            connected_nodes = g[node - 1]
            # print("n_edges for {} is {}".format(node, n_edges))
            for node_c in connected_nodes:
                if dis[node_c - 1] == -1:
                    dis[node_c - 1] = distance
                    q.append(node_c)

    del dis[s - 1]

    return dis


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
