#!/bin/python3

import math
import os
import random
import re
import sys

cut_count = 0


def node_count(t_from, t_to, node):
    global cut_count
    n_edges = []
    starts = [i for i in range(len(t_to)) if t_to[i] == node]

    count = 1
    for si in starts:
        e = t_from[si]
        count += node_count(t_from, t_to, e)

    if count % 2 == 0:
        cut_count += 1
    return count


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    # DSF algorithm. It doesn't matter in-order, pre-order, or post-order
    global cut_count
    cut_count = 0

    node_count(t_from, t_to, 1)
    # note the root is always an even number but can't cut
    return cut_count - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
