#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumLoss function below.

def minimumLoss(price):
    min_lost = sys.maxsize
    sort_price = []
    for index, p in enumerate(price):
        sort_price.append((p, index))
    sort_price.sort(key=lambda u: u[0], reverse=True)
    # print(sort_price)
    for i in range(0, len(sort_price) - 1):
        pr1 = sort_price[i]
        pr2 = sort_price[i + 1]
        if pr1[1] < pr2[1]:
            min_lost = min(min_lost, pr1[0] - pr2[0])

    #    for bi in range(len(price)):
    #        for si in range(bi + 1, len(price)):
    #            if price[si] - price[bi] < 0:
    #                min_lost = min(min_lost, price[bi] - price[si])

    return min_lost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
