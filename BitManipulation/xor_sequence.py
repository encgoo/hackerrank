#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the xorSequence function below.
def xorSequence(l, r):
    pre_computed = [0, 1, 2, 2, 6, 7, 0, 0]

    lacc = 0
    racc = 0

    if l > 0:
        l -= 1

    l8 = l % 8
    check_lst = [6, 7, 2, 3]
    if l8 not in check_lst:
        lacc = pre_computed[l8] + (l // 8) * 8
    elif l8 in [2, 3]:
        lacc = 2

    r8 = r % 8
    if r8 not in check_lst:
        racc = pre_computed[r8] + (r // 8) * 8
    elif r8 in [2, 3]:
        racc = 2

    return lacc ^ racc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
