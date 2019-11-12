#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the equal function below.
def count_steps(i):
    tmp = i
    count = int(tmp / 5)
    tmp = tmp % 5
    count += int(tmp / 2)
    tmp = tmp % 2
    count += tmp
    return count


def equal(arr):
    min_value = min(arr)

    count = sys.maxsize
    for i in range(4):
        tmp_count = 0
        for c in arr:
            tmp_count += count_steps(c - min_value + i)

        count = min(count, tmp_count)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
