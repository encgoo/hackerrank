#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
# Complete the beautifulPath function below.
def add_to_queue(q, i, cost, node_costs):
    # Check if this cost already exists
    if node_costs[i][cost]:
        # don't add
        return
    #print("adding i {} with cost {}".format(i, cost))
    node_costs[i][cost] = True
    q.append((i, cost))

def beautifulPath(edges, A, B, n):
    # simplify edges first
    edges_ = [[] for i in range(n)]
    for e in edges:
        # convert to 0 base
        edges_[e[0] - 1].append((e[1] - 1, e[2]))
        edges_[e[1] - 1].append((e[0] - 1, e[2]))

    #print (edges_)
    node_costs = [[False]*2048 for i in range(n)]

    # initialize node_costs with A
    node_costs[A - 1][0] = True
    # put A into a queue
    q = deque([(A - 1, 0)])

    while len(q) > 0:
        # pop one from the q
        node, cost = q.popleft()
        rs = edges_[node]
        for r in rs:
            next_node = r[0]
            next_cost = r[1] | cost
            add_to_queue(q, next_node, next_cost, node_costs)

    #print(node_costs[B-1])
    ret = -1
    for index in range(len(node_costs[B - 1])):
        if node_costs[B - 1][index]:
            ret = index
            break
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    AB = input().split()

    A = int(AB[0])

    B = int(AB[1])

    result = beautifulPath(edges, A, B, n)

    fptr.write(str(result) + '\n')

    fptr.close()
