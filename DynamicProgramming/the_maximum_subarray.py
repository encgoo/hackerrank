#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    global sum_
    sum_ = [None] * (len(arr) + 1)
    max_v = max(arr)
    sum_subsequence = 0
    if max_v > 0:
        for c in arr:
            if c > 0:
                sum_subsequence += c
        # Use Kadane's algorithm
        sum_subarray = -sys.maxsize
        cur_sum = 0
        for c in arr:
            cur_sum = max(0, cur_sum + c)
            sum_subarray = max(sum_subarray, cur_sum)
    else:
        sum_subsequence = max_v
        sum_subarray = max_v


    return [sum_subarray, sum_subsequence]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
