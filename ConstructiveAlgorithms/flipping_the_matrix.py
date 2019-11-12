#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def get_lr_mirror(sz, i, j):
    return i, sz - 1 - j
def get_ud_mirror(sz, i, j):
    return sz - 1 - i, j
def get_cross_mirror(sz, i, j):
    return sz - 1 -i, sz -1 - j

def flippingMatrix(matrix):
    count = 0
    n_2 = len(matrix)
    n = int(n_2/2)

    for i in range(n):
        for j in range(n):
            lr = get_lr_mirror(n_2, i, j)
            ud = get_ud_mirror(n_2, i, j)
            cr = get_cross_mirror(n_2, i, j)
            tmp1 = max(matrix[i][j], matrix[lr[0]][lr[1]])
            tmp2 = max(matrix[ud[0]][ud[1]], matrix[cr[0]][cr[1]])
            count += max(tmp1, tmp2)

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
