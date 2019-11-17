#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pylons function below.
def pylons(k, arr):
    ptr = 0
    decision_dist = k
    last_good_pos = -1
    ret = 0
    while ptr < len(arr):
        while ptr < decision_dist and ptr < len(arr):
            if arr[ptr] == 1:
                last_good_pos = ptr
            ptr += 1

        if last_good_pos == -1:
            ret = -1
            break
        else:
            # build in the last good location
            print(last_good_pos)
            ret += 1
            # if this one can cover to the end, then done
            if last_good_pos + k >= len(arr):
                break
            # reset ptr, decision_dist, and last_good_pos
            ptr = last_good_pos + 1
            decision_dist = last_good_pos + 2 * k
            last_good_pos = -1

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
