#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cipher function below.
def cipher(k, s):
    out_list = [int(s[0])]
    tmp_acc = [int(s[0])]
    ptr = 1
    while ptr <= len(s) - k:
        b = int(s[ptr])
        b = tmp_acc[-1] ^ b

        if len(tmp_acc) >= k:
            b = tmp_acc[-k] ^ b

        out_list.append(b)
        tmp_acc.append(tmp_acc[-1] ^ out_list[-1])
        ptr += 1
    l = [str(d) for d in out_list]
    return ''.join(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()
