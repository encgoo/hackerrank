#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the absolutePermutation function below.

def absolutePermutation(n, k):
    if k >= n:
        return [-1]
    if k == 0:
        return [i for i in range(1, n + 1)]

    if n % k != 0 or (n / k) % 2 != 0:
        return [-1]

    if n == 2 * k:
        l = [i for i in range(1 + k, n + 1)]
        r = [i for i in range(1, 1 + k)]
        l.extend(r)
        return l
    else:
        up = True
        ret = []
        for i in range(int(n / k)):
            for j in range(1, k + 1):
                offset = k if up else -k
                ret.append(i * k + j + offset)
            up = up is False
        return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
