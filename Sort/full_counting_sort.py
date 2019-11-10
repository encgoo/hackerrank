#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    # Use insertion sort to sort arr first, because it is stable
    # first sort arr[0] and arr[1]
    if arr[0][0] > arr[1][0]:
        arr[0], arr[1] = arr[1], arr[0]
    arr[0][1] = '-'
    arr[1][1] = '-'
    for i in range(2, len(arr)):
        if i < len(arr)/2:
            arr[i][1] = '-'
        if arr[i][0] < arr[0][0]:
            tmp = arr[i]
            arr[1: i + 1] = arr[:i]
            arr[0] = tmp
        elif arr[i][0] < arr[i - 1][0]:
            for j in range(i - 1):
                if int(arr[j][0]) <= int(arr[i][0]) < int(arr[j + 1][0]):
                    tmp = arr[i]
                    arr[j + 2: i + 1] = arr[j + 1: i]
                    arr[j + 1] = tmp
    ret = " ".join([e[1] for e in arr])
    print(ret)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
