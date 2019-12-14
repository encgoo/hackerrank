#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stoneDivision function below.

def count_div(n, s, record):
    if n in record:
        return record[n]

    possibles = []
    for x in s:

        if n%x == 0 and n != x:
            possibles.append(x)
    if len(possibles) == 0:
        record[n] = 0
        return 0

    max_count = 0
    for i in range(0, len(possibles)):
        x = possibles[i]
        max_count = max(1 + int(n/x)*count_div(x, s, record), max_count)
    record[n] = max_count
    return max_count

def stoneDivision(n, s):
    record = {}
    count = count_div(n, s, record)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()
