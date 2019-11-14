#!/bin/python3

import math
import os
import random
import re
import sys
import hashlib


# Complete the sherlockAndAnagrams function below.
def make_str(key_lst):
    ret = ""
    for i in range(len(key_lst)):
        if key_lst[i] > 0:
            ret += str(key_lst[i]) + chr(i + ord('a'))
    return ret


def sherlockAndAnagrams(s):
    sz = len(s)
    d = dict()
    for start in range(sz):
        for end in range(start + 1, sz + 1):
            key = [0] * 26
            for i in range(start, end):
                index = ord(s[i]) - ord('a')
                key[index] += 1
            key_str = make_str(key)
            if key_str not in d:
                d[key_str] = 1
            else:
                d[key_str] += 1

    count = 0
    # print(d)
    for k in d:
        if d[k] >= 2:
            count += int(d[k] * (d[k] - 1) / 2)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
