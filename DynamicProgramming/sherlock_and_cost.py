#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    s_max = abs(1 - B[1])
    s_min = abs(B[0] - 1)

    for i in range(2, len(B)):
        tmp = s_max
        s_max = max(s_max + abs(B[i] - B[i - 1]), s_min + abs(B[i] - 1))
        s_min = tmp + abs(1 - B[i-1])

    return max(s_max, s_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
