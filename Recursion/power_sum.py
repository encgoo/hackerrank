#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
count = 0


def power_sum_cur(X, N, i, cur_sum):
    global count
    if cur_sum + i ** N == X:
        count += 1
        return

    if i ** N > X:
        return

    tmp = cur_sum + i ** N
    if tmp < X:
        power_sum_cur(X, N, i + 1, cur_sum)
        power_sum_cur(X, N, i + 1, tmp)


def powerSum(X, N):
    global count
    count = 0
    power_sum_cur(X, N, 1, 0)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
