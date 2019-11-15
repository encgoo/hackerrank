#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def abbreviation(a, b):
    mapping = [[False] * (len(a) + 1) for i in range(len(b) + 1)]
    # initialize.
    # take nothing from a or b
    mapping[0][0] = True
    # first char
    mapping[1][1] = a[0].upper() == b[0].upper()
    mapping[0][1] = a[0].lower() == a[0]  # can remove a lower case from a
    mapping[1][0] = False  # can't remove from b

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[j - 1].upper() == b[i - 1].upper():
                mapping[i][j] = mapping[i - 1][j - 1]
                if a[j - 1].lower() == a[j - 1]:
                    mapping[i][j] = mapping[i][j] or mapping[i][j - 1]
            else:
                if a[j - 1].lower() == a[j - 1]:
                    # try to remove one from a
                    # print("{} {}".format(a[j-1], mapping[i][j-1]))
                    mapping[i][j] = mapping[i][j - 1]
                else:
                    mapping[i][j] = False

    # print(mapping[-3:])
    if mapping[len(b)][len(a)]:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
