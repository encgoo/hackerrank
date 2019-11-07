#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.

def union_connect(connects, s, e, clusters):
    # connect them
    if e not in clusters:
        connects[e - 1] = s
        if s not in clusters:
            clusters[s] = (1, 2)
        else:
            # both cities and roads increased by one
            clusters[s] = (clusters[s][0] + 1, clusters[s][1] + 1)
    else:
        connects[s - 1] = e
        if s not in clusters:
            clusters[e] = (clusters[e][0] + 1, clusters[e][1] + 1)
        else:
            clusters[e] = (clusters[s][0] + clusters[e][0] + 1,
                           clusters[s][1] + clusters[e][1])
            del clusters[s]


def find_root(connects, city):
    # given a city find the root, if there is one
    ret = city
    tmp = city
    while tmp != -1 and connects[tmp - 1] != -1:
        ret = connects[tmp - 1]
        tmp = connects[tmp - 1]
    return ret


def roadsAndLibraries(n, c_lib, c_road, cities):
    # store the cluster head and the min number of roads to connect all
    # cites in this cluster
    clusters = {}
    connects = [-1] * n

    for r in cities:
        s = r[0]
        e = r[1]
        root_s = find_root(connects, s)
        root_e = find_root(connects, e)
        if root_s != root_e:
            union_connect(connects, root_s, root_e, clusters)

    cost = 0
    # first fill all the cities not connected to any other
    isolated = [value for index, value in enumerate(connects) if value == -1 and index + 1 not in clusters]
    # lib for each of them
    cost += len(isolated)*c_lib
    for k in clusters:
        c = clusters[k]
        num_roads = c[0]
        num_cities = c[1]
        cost += min(c_lib*num_cities, c_lib + c_road*num_roads)
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
