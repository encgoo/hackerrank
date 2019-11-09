#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def count_swap(arr):
    sorted_arr = sorted(arr)
    pos_dict = {}
    for index, value in enumerate(sorted_arr):
        pos_dict[value] = index

    arr_cp = arr[:]
    # Check each of it
    count = 0
    for i in range(len(arr_cp)):
        #
        # For each location, keep on swaping until this location is
        # good
        done = False
        while not done:
            tmp = arr_cp[i]
            if pos_dict[tmp] == i:
                done = True
            else:
                count += 1
                arr_cp[i], arr_cp[pos_dict[tmp]] = arr_cp[pos_dict[tmp]], arr_cp[i]

    return count


def lilysHomework(arr):
    return min(count_swap(arr), count_swap(arr[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
