#!/bin/python3

import os
import sys

#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    total_time_needed = sum(arr)
    if total_time_needed > 2*g:
        return "NO"
    if max(arr) > g:
        return "NO"

    #
    # max_holding[i][j] store the information stores the following infomration
    # when g = i, given arr[0]...arr[j], the maximum to be done within g = i 
    #
    max_holding = [[0]* (g + 1) for i in range(len(arr) + 1)]

    # initialize
    for i in range(1, len(arr) + 1):
        for g_i in range(1, g + 1):
            if g_i < arr[i - 1]:
                # There is no way to put the new arr[i - 1] into g_i
                # Same as without arr[i], or say i - 1 case
                max_holding[i][g_i] = max_holding[i - 1][g_i]
            else:
                # it is possible to put arr[i - 1] into g_i
                # two possiblities, take the max one
                max_holding[i][g_i] = max(max_holding[i - 1][g_i],
                max_holding[i - 1][g_i - arr[i - 1]] + arr[i - 1])

    if total_time_needed - max_holding[len(arr)][g] <= g:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g, arr)

        fptr.write(result + '\n')

    fptr.close()
