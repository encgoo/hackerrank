#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def union_nodes(connected, s, e):
    connected[s] = e

def find_root(connected, s):
    ret = s
    while connected[ret] != -1:
        ret = connected[ret]
    return ret

def journeyToMoon(n, astronaut):
    # Use find and union algorithm
    connected = [-1] * n

    for p in astronaut:
        s = p[0] - 1
        e = p[1] - 1
        root_s = find_root(connected, s)
        root_e = find_root(connected, e)

        if root_s != root_e:
            union_nodes(connected, root_s, root_e)

    countries = {}
    for a_i in range(n):
        if connected[a_i] == -1:
            if a_i in countries:
                countries[a_i] += 1
            else:
                countries[a_i] = 1
        else:
            root = find_root(connected, a_i)

            if root in countries:
                countries[root] += 1
            else:
                countries[root] = 1

    count = 0
    cs = list(countries.keys())

    acc = 0
    for i in range(len(cs)):
        count += countries[cs[i]]*acc
        acc += countries[cs[i]]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
