#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.

def check_swap(arr):
    swap_points = []
    # print(len(arr))
    for i in range(len(arr) - 1):
        # print("{}, {}, {}, {}".format(i, arr[i], arr[i + 1], arr[i] > arr[i + 1]))
        if arr[i] > arr[i + 1]:
            if len(swap_points) >= 2:
                return False
            else:
                swap_points.append(i)
    # print(swap_points)
    if len(swap_points) == 0:
        print("yes")
        return True
    elif len(swap_points) == 1:
        # check if we can swap i and i + 1
        i = swap_points[0]
        if (i == len(arr) - 2 or arr[i] < arr[i + 2]) and (i == 0 or arr[i + 1] > arr[i - 1]):
            print("yes")
            print("swap {} {}".format(i + 1, i + 2))
            return True
        else:
            return False
    else:
        assert len(swap_points) == 2
        i = swap_points[0]
        j = swap_points[1] + 1
        if (j == len(arr) - 1 or arr[i] < arr[j + 1]) and (i == 0 or arr[j] > arr[i - 1]):
            print("yes")
            print("swap {} {}".format(i + 1, j + 1))
            return True
        else:
            return False


def check_reverse(arr):
    start = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            start = i
            break
    end = len(arr) - 1
    for i in range(start, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            end = i
            break
    for i in range(end, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print("no")
            return False

    if (start == 0 or arr[end] > arr[start - 1]) and (end == len(arr) - 1 or arr[start] < arr[end + 1]):
        print("yes")
        print("reverse {} {}".format(start + 1, end + 1))
        return True
    else:
        print("no")
        return False


def almostSorted(arr):
    possible = check_swap(arr)

    if possible is False:
        check_reverse(arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
