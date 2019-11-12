#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
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
def find_root(connected, i):
    # find the root for the input i node, using the connected linked list
    root_index = i
    while connected[root_index] != -1:
        root_index = connected[root_index]

    return root_index

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    # Kruskals is similar to Union and Find

    # first we need to sort the edges. But list of edges, and sort it
    # accroding to the weight
    edges = []
    for i in range(len(g_from)):
        # Use a tuple to store edge information
        edges.append((g_from[i], g_to[i], g_weight[i]))
    # sort edges
    edges.sort(key=lambda u:u[2])

    # linked list for connected nodes.
    connected = [-1]*g_nodes
    ret = 0
    for e in edges:
        start = e[0] - 1
        end = e[1] - 1
        root_start = find_root(connected, start)
        root_end = find_root(connected, end)
        if root_start != root_end:
            # Adding this edge to the existing tree does NOT found a loop
            # add its weight to the total sum
            ret += e[2]
            # Link these two nodes. It does not matter linking root_start to
            # root_end or root_end to root_start
            connected[root_start] = root_end

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')
    fptr.close()
