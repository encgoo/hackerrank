#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    if n == 0:
        return 0

    candy_kid = [0] * n
    # at least one candy for each kid
    num_candies_to_give = 1
    candy_kid[0] = num_candies_to_give

    for index in range(1, len(arr)):
        if arr[index] > arr[index - 1]:
            # need to give more candy
            num_candies_to_give += 1
        else:
            num_candies_to_give = 1
        candy_kid[index] = num_candies_to_give

    # reset
    num_candies_to_give = 1
    # init
    total_candies = candy_kid[-1]
    for index in range(len(arr) - 2, -1, -1):
        if arr[index] > arr[index + 1]:
            num_candies_to_give += 1
        else:
            num_candies_to_give = 1

        total_candies += max(candy_kid[index], num_candies_to_give)

    return total_candies

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
