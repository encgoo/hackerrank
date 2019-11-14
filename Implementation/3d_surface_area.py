#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the surfaceArea function below.
def get_A(A, i, j):
    if i >= 0 and j >= 0 and i < len(A) and j < len(A[0]):
        return A[i][j]
    else:
        return 0


def surfaceArea(A):
    surface = 0
    # top and bottom surfaces are always fixed
    surface += 2 * len(A) * len(A[0])

    # now go through each location and check its four edges
    # the top and bottom are already taken into account.
    for i in range(len(A)):
        for j in range(len(A[0])):
            surface += max(0, A[i][j] - get_A(A, i + 1, j))
            surface += max(0, A[i][j] - get_A(A, i, j + 1))
            surface += max(0, A[i][j] - get_A(A, i - 1, j))
            surface += max(0, A[i][j] - get_A(A, i, j - 1))

    return surface


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
