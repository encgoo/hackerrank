#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    rnd = 1
    cost = 0

    index = len(c) - 1
    c.sort()
    while index >= 0:
        for i in range(k):
            tmp = index - i
            if tmp < 0:
                break
            else:
                cost += rnd * c[tmp]
        index -= k
        rnd += 1

    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
