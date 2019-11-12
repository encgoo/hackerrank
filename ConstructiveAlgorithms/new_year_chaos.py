#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    org_list = []
    for index in range(len(q)):
        org_list.append((q[index], index))

    org_list.sort(key=lambda u: u[0])
    count = 0
    for i in range(len(q)):
        j_index = 0
        for j in range(i, len(q)):
            if org_list[j][1] == i:
                j_index = j
                break

        if j_index - i > 2:
            count = sys.maxsize
            break
        count += j_index - i
        tmp = j_index
        while tmp != i:
            org_list[tmp], org_list[tmp - 1] = org_list[tmp - 1], org_list[tmp]
            tmp -= 1

    if count == sys.maxsize:
        print("Too chaotic")
    else:
        print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
