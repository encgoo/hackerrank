#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def one_step(n):
    tmp = n
    power = 0
    while tmp > 1:
        power += 1
        tmp = tmp >> 1
    power_2 = 1<< power
    if power_2 == n:
        return int(power_2/2)
    else:
        return n - power_2

def counterGame(n):
    if n == 1:
        return "Richard"
    tmp = n
    steps = 0
    while tmp > 1:
        tmp = one_step(tmp)
        steps += 1
    #print(steps)
    if steps%2 == 0:
        return "Richard"
    return "Louise"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()