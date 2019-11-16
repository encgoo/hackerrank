#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    num_diff_coins = len(c)
    max_ways = [[0] * (n + 1) for _ in range(num_diff_coins + 1)]

    for i in range(0, num_diff_coins + 1):
        # initialize the outside case to be 1
        max_ways[i][0] = 1
    #
    # Further initialize the one kind of coins case
    #
    for n_j in range(1, n + 1):
        if n_j % c[0] == 0:
            # Since we have only on kind of coins there is only
            # one way if n_j%c[0] = 0
            max_ways[1][n_j] = 1

    for i in range(2, num_diff_coins + 1):
        for n_j in range(1, n + 1):
            if n_j < c[i - 1]:
                # can't put it in. same as c[i -1] not used at all
                max_ways[i][n_j] = max_ways[i - 1][n_j]
            else:
                # at least max_ways[i - 1][n_j]
                max_ways[i][n_j] = max_ways[i - 1][n_j]
                tmp = n_j - c[i - 1]
                while tmp >= 0:
                    max_ways[i][n_j] += max_ways[i - 1][tmp]
                    tmp -= c[i - 1]

    # print(max_ways)
    return max_ways[num_diff_coins][n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
