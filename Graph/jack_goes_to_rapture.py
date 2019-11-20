#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
from collections import deque
def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    shortest = [sys.maxsize] * g_nodes
    # always convert adjacent list to this
    g = [[] for _ in range(g_nodes)]
    for i in range(len(g_from)):
        g[g_from[i] - 1].append((g_to[i] - 1, g_weight[i]))
        g[g_to[i] - 1].append((g_from[i] - 1, g_weight[i]))

    # intitialize
    shortest[0] = 0
    node_in_q = [False] * g_nodes
    q = deque([0]) # q use 0-base
    node_in_q[0] = True

    while len(q) > 0:
        node = q.popleft() # 0-based
        node_in_q[node] = False
        connected_nodes = g[node] #0 based
        for c_node in connected_nodes:
             nd = c_node[0]
             w = max(0, c_node[1] - shortest[node]) + shortest[node]
             if w < shortest[nd]:
                shortest[nd] = w
                if node_in_q[nd] is False:
                    q.append(nd)
                    node_in_q[nd] = True
    #print(shortest)
    if shortest[g_nodes - 1] < sys.maxsize:
        print(str(shortest[g_nodes - 1]))
    else:
        print("NO PATH EXISTS")

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
