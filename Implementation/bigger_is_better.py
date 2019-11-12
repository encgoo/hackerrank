#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    # start from the end to beginning, if always ascending, then no answer

    index = len(w) - 2
    while index >= 0 and ord(w[index]) >= ord(w[index + 1]):
        index -= 1

    if index < 0:
        return "no answer"

    # scan again from the end
    j = len(w) - 1
    while w[j] <= w[index]:
        j -= 1

    w_lst = list(w)

    w_lst[index], w_lst[j] = w_lst[j], w_lst[index]

    w_lst[index + 1:] = w_lst[len(w_lst) - 1: index:-1]
    return "".join(w_lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
