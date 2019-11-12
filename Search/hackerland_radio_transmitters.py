#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    s = set(x)
    x = list(s)
    x.sort()
    count = 0

    ptr = 0

    while ptr < len(x):
        # figure out where to put the next station
        # search range of k
        start = 0
        station_pos_index = start
        while start <= k and ptr + start < len(x):
            if x[ptr + start] - x[ptr] <= k:
                station_pos_index = ptr + start
            else:
                break
            start += 1
        # install a station
        count += 1
        # figure out how far this station cover
        cover_ptr = station_pos_index
        start = 0
        end_ptr = cover_ptr
        #if cover_ptr < len(x):
        #    print("station at {}".format(x[cover_ptr]))
        while start <= k and cover_ptr + start < len(x):
            if x[cover_ptr + start] - x[cover_ptr] <= k:
                end_ptr = cover_ptr + start
                start += 1
            else:
                break
        #print("station {}, end cover {}".format(x[station_pos_index], end_ptr))
        ptr = end_ptr + 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
