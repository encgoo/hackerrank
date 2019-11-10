#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the activityNotifications function below.
def get_median(period, index, isOdd):
    if isOdd is False:
        # d is even, we need index and index + 1
        count = 0
        ptr = 0
        while count < index:
            count += period[ptr]
            ptr += 1
        ptr -= 1
        if count >= index + 1:
            # ptr covers both index and index
            return ptr
        else:
            tmp = ptr + 1
            # find the next none-zero count
            while period[tmp] == 0:
                tmp += 1
            return (ptr + tmp) / 2
    else:
        # d is odd
        count = 0
        ptr = 0
        while count <= index:
            count += period[ptr]
            ptr += 1

        return ptr - 1


def remake_period(period, pre_exp, next_exp):
    period[pre_exp] -= 1
    period[next_exp] += 1


def activityNotifications(expenditure, d):
    period = [0] * 201

    for i in range(d):
        period[expenditure[i]] += 1

    index = int(d / 2)
    isOdd = d % 2 == 1

    warnings = 0
    for i in range(d, len(expenditure)):
        median = get_median(period, index, isOdd)

        if expenditure[i] >= 2 * median:
            warnings += 1
        remake_period(period, expenditure[i - d], expenditure[i])

    return warnings


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
