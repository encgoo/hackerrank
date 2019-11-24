#!/bin/python3

import os
import sys

#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    # First of all a b c d are symmetric.
    # It makes sense to sort them first
    aa, bb, cc, dd = sorted([a, b, c, d])
    # Note they are all smaller than 3000
    total = [0] * 3001
    # for x^y, at most 4096-1
    cnt = [[0 for _ in range(4095)] for i in range(3001)]
    for i in range(1, aa + 1):
        for j in range(i, bb + 1):
            total[j] += 1
            cnt[j][i ^ j] += 1

    for i in range(1, 3001):
        total[i] += total[i-1]
        for j in range(4095):
            cnt[i][j] += cnt[i-1][j]
    ret = 0
    for i in range(1, cc + 1):
        for j in range(i, dd + 1):
            ret += total[i] - cnt[i][i ^ j]

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
