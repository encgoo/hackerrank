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

def find_closest_with_road(record, visited):
    min_dis = sys.maxsize
    ret_index = -1
    ret_k_index = -1
    for index in range(len(record)):
        for k_index in range(len(record[0])):
            if visited[index][k_index] is False:
                if record[index][k_index] < min_dis:
                    min_dis = record[index][k_index]
                    ret_index = index
                    ret_k_index = k_index

    return ret_index, ret_k_index


def find_min_path(complete_path, k):
    # filter out all the paths that can be alone
    single_paths= [p for p in complete_path if max(p[0]) < sys.maxsize]
    min_cost = sys.maxsize
    for p in single_paths:
        min_cost = min(min_cost, max(p[0]) + p[1])

    other_paths = [p for p in complete_path if max(p[0]) == sys.maxsize]

    # Since we have two cats, we look for two paths from all these
    for i in range(len(other_paths)):
        for j in range(i + 1, len(other_paths)):
            merge = list(map(min, zip(other_paths[i][0], other_paths[j][0])))
            if max(merge) < sys.maxsize:
                # This is a possible solution
                p1 = max(other_paths[i][0]) + other_paths[i][1]
                p2 = max(other_paths[j][0]) + other_paths[j][1]
                min_cost = min(min_cost, min(p1, p2))

    return min_cost

def is_completed(visited):
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] is False:
                return False

    return True
def shop(n, k, centers, roads):

    # Write your code here
    # keep track the distance and the fish types so far for each node
    record = [[sys.maxsize] * (k + 1) for i in range(n)]
    # visited shall be k favors as well
    visited = [[False] * (k + 1) for i in range(n)]

    center_fish_types = []
    for c in centers:
        fish_types = list(map(int, c.split()))
        center_fish_types.append(fish_types[1:])

    #
    # Since Dijkstra/greedy algorithm is using, we can get the min
    #

    # initialize the start node
    fish_types = center_fish_types[0]
    if len(fish_types) == 0:
        # allow no fish type to propagate
        record[0][0] = 0
    else:
        # don't allow no fish type to propagate
        for ii in range(n):
            visited[ii][0] = True
        for ii in fish_types:
            record[0][ii] = 0

    complete_path = []
    while is_completed(visited) is False:
        node_index, k_index = find_closest_with_road(record, visited)
        rds = [r for r in roads if r[0] == node_index + 1 or r[1] == node_index + 1]
        visited[node_index][k_index] = True
        for r in rds:
            # update a node this can reach
            a_node = r[0] if r[1] == node_index + 1 else r[1]
            a_node_fish_types = center_fish_types[a_node - 1]

            record[a_node - 1][k_index] = min(record[a_node - 1][k_index], record[node_index][k_index] + r[2])

            for t in a_node_fish_types:
                record[a_node - 1][t] = min(record[node_index][k_index] + r[2], record[a_node - 1][t])

            # check if this node is completed
            if (a_node == n):
                # Reach n, store the result
                complete_path.append((record[node_index][:], r[2]))

    return max(record[n - 1][1:])

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
