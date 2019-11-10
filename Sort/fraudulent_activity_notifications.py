#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def find_pos(l, i, j, item):
    # find where item can be inserted into a sorted list
    if i + 1 == j:
        if item >= l[i] and item < l[j]:
            return i
        elif item >= l[j]:
            return j
        else:
            return i - 1
    elif i == j:
        if item >= l[i]:
            return i
        else:
            return i - 1

    middle = int((j - i + 1) / 2)
    if item >= l[i + middle]:
        return find_pos(l, i + middle, j, item)
    else:
        return find_pos(l, i, i + middle - 1, item)

def get_median(l, index, isOdd):
    if isOdd:
        return l[index]
    else:
        return (l[index -1] + l[index] ) /2

def remake_period(period, pre_exp, next_exp):
    pos1 = find_pos(period, 0, len(period) - 1, pre_exp)
    pos2 = find_pos(period, 0, len(period) - 1, next_exp)

    # in place replacement
    if pos1 == pos2:
        period[pos1] = next_exp
    elif pos1 > pos2:
        period[pos2 + 1:pos1 + 1] = period[pos2: pos1]
        period[pos2] = next_exp
    else:
        period[pos1: pos2] = period[pos1 + 1: pos2 + 1]
        period[pos2] = next_exp


def activityNotifications(expenditure, d):
    period = expenditure[:d]

    period.sort()
    index = int( d /2)
    isOdd = d% 2 == 1

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
