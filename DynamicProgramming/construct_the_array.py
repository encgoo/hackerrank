#!/bin/python3

import math
import os
import random
import re
import sys
MOD = 10**9+7
# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    accu_0 = 0
    accu_1 = 1
    accu_tmp = 0

    k1 = k - 1
    k2 = k - 2

    for i in range(1, n - 1):
        accu_tmp = (accu_0*k2 + accu_1) % MOD
        accu_1 = (accu_0*k1) % MOD
        accu_0 = accu_tmp

    ret = (accu_0 * k2 + accu_1) % MOD
    if x == 1:
        ret = (accu_0 * k1) % MOD

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
