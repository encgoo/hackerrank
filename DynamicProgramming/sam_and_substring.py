#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    count = 0
    pre_digit = 0
    for i in range(len(n)):
        pre_digit = (pre_digit * 10 + int(n[i]) * (i + 1))%(10**9 + 7)
        count = (count + pre_digit)%(10**9 + 7)

    return int(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
