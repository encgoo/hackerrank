#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def visit_node(tree, visited, data, node_sum, i):
    children = tree[i]
    visited[i] = True
    if len(children) == 0:
        # leaf node
        node_sum[i] = data[i]
        return data[i]
    n_sum = data[i]
    for c in children:
        if visited[c] is False:
            n_sum += visit_node(tree, visited, data, node_sum, c)
    node_sum[i] = n_sum
    return node_sum[i]


def cutTheTree(data, edges):
    # Write your code here
    # rebuild a tree first. Use the first node as root node
    num_nodes = len(data)

    tree = [[] for _ in range(num_nodes)]
    for e in edges:
        tree[e[0] - 1].append(e[1] - 1)
        tree[e[1] - 1].append(e[0] - 1)

    visited = [False] * num_nodes

    # Now use recursion to traverse the tree
    node_sum = [-1] * num_nodes
    visit_node(tree, visited, data, node_sum, 0)
    total = node_sum[0]
    min_diff = node_sum[0]
    for i in range(1, num_nodes):
        min_diff = min(abs(total - 2 * node_sum[i]), min_diff)
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # the dfs can be pretty deep when n is big. Set this to a big limit.
    sys.setrecursionlimit(100000)

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
