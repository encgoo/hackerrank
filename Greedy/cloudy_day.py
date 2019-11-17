#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumPeople function below.
def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    clouds_over = [[] for _ in range(len(p))]
    assert len(p) == len(x)
    assert len(y) == len(r)
    clouds_cities = []
    for i in range(len(y)):
        clouds_cities.append((y[i] - r[i], i, -1))
        clouds_cities.append((y[i] + r[i], i, 1))
    # sort it
    clouds_cities.sort(key=lambda u: (u[0], u[2]))

    x_p = []
    for i in range(len(x)):
        x_p.append((x[i], p[i]))
    x_p.sort(key=lambda u:u[0])

    cur_cloud = []
    sunny_city_population = 0
    pre_cld = 0
    cld_ptr = 0
    cty_ptr = 0
    cloud_handled = -1

    one_cloud_population = {}
    most_one_cloud_population = 0
    while cld_ptr < len(clouds_cities) and cty_ptr < len(x):
        c_c = clouds_cities[cld_ptr]

        # edge case
        if x_p[cty_ptr][0] == c_c[0] and c_c[2] == -1:
            # First handle the cloude first
            cur_cloud.append(c_c[1])
            cloud_handled = c_c[1]
            if len(cur_cloud) == 0:
                sunny_city_population += x_p[cty_ptr][1]
            elif len(cur_cloud) == 1:
                # city covered by only one cloud
                if cur_cloud[0] not in one_cloud_population:
                    one_cloud_population[cur_cloud[0]] = x_p[cty_ptr][1]
                else:
                    one_cloud_population[cur_cloud[0]] += x_p[cty_ptr][1]
                most_one_cloud_population = max(most_one_cloud_population, one_cloud_population[cur_cloud[0]])

            cty_ptr += 1

        if pre_cld <= x_p[cty_ptr][0] <= c_c[0]:
            if len(cur_cloud) == 0:
                sunny_city_population += x_p[cty_ptr][1]
            elif len(cur_cloud) == 1:
                # city covered by only one cloud
                if cur_cloud[0] not in one_cloud_population:
                    one_cloud_population[cur_cloud[0]] = x_p[cty_ptr][1]
                else:
                    one_cloud_population[cur_cloud[0]] += x_p[cty_ptr][1]
                most_one_cloud_population = max(most_one_cloud_population, one_cloud_population[cur_cloud[0]])

            cty_ptr += 1
        else:
            if c_c[2] == -1:
                # start of cloud
                if c_c[1] != cloud_handled:
                    cur_cloud.append(c_c[1])
            elif c_c[2] == 1:
                # end of cloud
                cur_cloud.remove(c_c[1])
            pre_cld = c_c[0]
            cld_ptr += 1

    for i in range(cty_ptr, len(x)):
        sunny_city_population += x_p[i][1]


    return most_one_cloud_population + sunny_city_population


infile = open("cd.txt", "r")

n = int(infile.readline())

p = list(map(int, infile.readline().rstrip().split()))

x = list(map(int, infile.readline().rstrip().split()))

m = int(infile.readline())

y = list(map(int, infile.readline().rstrip().split()))

r = list(map(int, infile.readline().rstrip().split()))

result = maximumPeople(p, x, y, r)
print(result)


"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
"""