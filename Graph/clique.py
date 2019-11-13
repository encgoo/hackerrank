#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def check(n, l):
    ret = (n*n - (n%l)*math.ceil(n/l)**2 - (l - n%l)*math.floor(n/l)**2)/2
    return int(ret)
def clique(n, m):
    # Write your code here
    # https://en.wikipedia.org/wiki/Tur%C3%A1n_graph
    k = math.ceil(n*n/(n*n - 2*m))
    while m > check(n, k):
        k += 1

    return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
