#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

from collections import deque

def add_to_queue(q, record, index, mask, min_dist):
    old_dist = record[index][mask]
    if old_dist < min_dist:
        # this new update is worse than the one in record. No need to add to the q
        return
    old_q_item = (index, mask, old_dist)
    if old_q_item in q:
        q.remove((index, mask, old_dist))

    record[index][mask] = min_dist
    q.append((index, mask, min_dist))


def shop(n, k, centers, roads):

    # Write your code here
    # keep track the distance and the fish type combinations so far for each node
    record = [[sys.maxsize] * (2**k) for i in range(n)]
    roads_ =[[] for i in range(n + 1)]

    for r in roads:
        roads_[r[0]].append((r[1], r[2]))
        roads_[r[1]].append((r[0], r[2]))

    center_fish_types = []
    for c in centers:
        fish_types = list(map(int, c.split()))
        fish_type_mask = 0
        for j in range(1, fish_types[0] + 1):
            fish_type_mask |= 1 << fish_types[j] - 1
        center_fish_types.append(fish_type_mask)

    #
    # Since Dijkstra/greedy algorithm is using, we can get the min
    #

    # initialize the start node
    record[0][center_fish_types[0]] = 0
    # find_closest_with_road is going to check if there is any more
    # node to update
    q = deque([(0, center_fish_types[0], 0)])
    while len(q) > 0:
        # node_index is 0 based
        sz = len(q)
        node_index, mask, dis = q.popleft()
        rds = roads_[node_index + 1]

        for r in rds:
            # update a node this can reach
            a_node = r[0]
            current_center_mask = center_fish_types[a_node - 1]
            next_mask = mask | current_center_mask
            add_to_queue(q, record, a_node - 1, next_mask, dis + r[1])

    best_time = sys.maxsize
    for i in range(len(record[0])):
        for j in range(len(record[0])):
            if i|j == 2**k -1:
                best_time = min(best_time, max(record[n - 1][i], record[n-1][j]))

    return best_time

if __name__ == '__main__':
    with open("ss_data.txt", "r") as infile:

        first_multiple_input = infile.readline().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        k = int(first_multiple_input[2])

        centers = []

        for _ in range(n):
            centers_item = infile.readline()
            centers.append(centers_item)

        roads = []

        for _ in range(m):
            roads.append(list(map(int, infile.readline().rstrip().split())))

        res = shop(n, k, centers, roads)
        print(res)
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()
    """
