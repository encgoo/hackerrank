#!/bin/python3

import os
import sys

#
# Complete the chocolateInBox function below.
#
def chocolateInBox(arr):
    #
    # Write your code here.
    #
    b = 0
    for i in arr:
        b ^= i
    count = sum([int(i^b < i) for i in arr])
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
