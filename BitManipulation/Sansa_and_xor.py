#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):
    sz = len(arr)
    if sz %2 == 0:
        return 0

    acc = 0
    for index in range(len(arr)):
        if index % 2 == 0:
            acc = acc ^ arr[index]
    return acc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
