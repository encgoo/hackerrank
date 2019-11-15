#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    # use a char list to count
    counts = [0] * 26
    for c in s:
        counts[ord(c) - ord('a')] += 1

    non_zeros = [counts[i] for i in range(26) if counts[i] > 0]
    # print(non_zeros)
    assert len(non_zeros) > 0
    if len(non_zeros) == 1:
        return "YES"
    if len(non_zeros) == 2:
        if abs(non_zeros[0] - non_zeros[1]) <= 1:
            return "YES"
        else:
            return "NO"
    else:
        diff_counts = set(non_zeros)
        if len(diff_counts) == 1:
            return "YES"
        if len(diff_counts) == 2:
            smaller = min(diff_counts)
            if smaller == 1:
                count_smaller = [c for c in non_zeros if c == smaller]
                if len(count_smaller) == 1:
                    return "YES"
            bigger = max(diff_counts)
            if bigger - smaller == 1:
                count_bigger = [c for c in non_zeros if c == bigger]
                if len(count_bigger) == 1:
                    return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
