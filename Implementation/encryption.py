#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def find_dim(sz):
    w = 0
    l = 0
    sqr = math.sqrt(sz)
    flr = int(math.floor(sqr))
    cl = int(math.ceil(sqr))

    if cl * flr < sz:
        w = cl
        l = cl
    else:
        w = flr
        l = cl

    return (w, l)


def encryption(s):
    # first remove space
    s_tmp = s.replace(' ', '')
    sz = len(s_tmp)
    row, col = find_dim(sz)

    mat = [s[start * col: start * col + col] for start in range(row)]

    ret = [''] * col

    for i in range(row):
        for j in range(col):
            try:
                ret[j] += mat[i][j]
            except:
                # read all already
                break

    return " ".join(ret)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
