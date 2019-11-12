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

def can_update_neighbor(record, roads, index, mask, center_fish_types):
    # all roads from/to this shop
    rds = [r for r in roads if r[0] == index + 1 or r[1] == index + 1]
    can_update = False
    for r in rds:
        neighbor = r[0] if r[1] == index + 1 else r[1]
        neighbor_mask = center_fish_types[neighbor - 1]
        new_mask = mask | neighbor_mask
        if record[neighbor - 1][new_mask] > record[index][mask] + r[2]:
            can_update = True
            break

    return can_update


def find_closest_with_road(record, roads, center_fish_types):
    min_dis = sys.maxsize
    ret_index = -1
    ret_k_index = -1
    for index in range(len(record)):
        for mask in range(len(record[0])):
            #
            #   Make sure this node can cause update on neighbors.
            #
            if can_update_neighbor(record, roads, index, mask, center_fish_types):
                if record[index][mask] < min_dis:
                    min_dis = record[index][mask]
                    ret_index = index
                    ret_k_index = mask
                    break

    return ret_index, ret_k_index


def shop(n, k, centers, roads):

    # Write your code here
    # keep track the distance and the fish type combinations so far for each node
    record = [[sys.maxsize] * (2**k) for i in range(n)]

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
    while True:
        node_index, mask = find_closest_with_road(record, roads, center_fish_types)
        if node_index == -1:
            break
        rds = [r for r in roads if r[0] == node_index + 1 or r[1] == node_index + 1]

        for r in rds:
            # update a node this can reach
            a_node = r[0] if r[1] == node_index + 1 else r[1]
            current_center_mask = center_fish_types[a_node - 1]
            next_mask = mask | current_center_mask
            record[a_node - 1][next_mask] = min(record[a_node - 1][next_mask], record[node_index][mask] + r[2])


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
