#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSort function below.
def countSort(arr):
    # Note we don't really need to sort. The index are already 1-m (m<n because
    # repeating allowed)
    sz = len(arr)
    ret = [""] * sz

    for i in range(sz):
        if i < sz / 2:
            ret[int(arr[i][0])] += '-' + ' '
        else:
            ret[int(arr[i][0])] += arr[i][1] + ' '

    print(''.join(ret))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

