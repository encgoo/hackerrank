#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    # bottom up approach
    profit = 0

    index = len(prices) - 1
    cur_highest = 0
    while index >= 0:
        #print("p {}, h {}".format(profit, cur_highest))
        if prices[index] > cur_highest:
            cur_highest = prices[index]
        else:
            profit += cur_highest - prices[index]
        index -= 1
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
