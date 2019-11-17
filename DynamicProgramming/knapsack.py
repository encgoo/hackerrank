#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    kp = [[0] * (k + 1) for _ in range(len(arr) + 1)]

    # intialize j = 1 row
    for i in range(1, k + 1):
        kp[1][i] = i - i%arr[0]

    for j in range(2, len(arr) + 1):
        for i in range(1, k + 1):
            if kp[j - 1][i] == i:
                # no need to do anything further
                kp[j][i] = kp[j - 1][i]
            else:
                # see if we can improve by using the new arr[j - 1]
                kp[j][i] = kp[j - 1][i]
                i_ptr = i - arr[j - 1]
                while i_ptr >= 0:
                    kp[j][i] = max(kp[j][i], kp[j][i_ptr] + arr[j - 1])
                    i_ptr -= arr[j - 1]

    #print (kp)
    return kp[len(arr)][k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
