#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    #python can automatically up-cast 
    tmp = n
    ret = 1
    while tmp > 1:
        ret *= tmp
        tmp -= 1

    print(ret)
    return ret


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)