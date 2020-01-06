#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the redJohn function below.
def count_prime_sieve(n):
    """
    Find number of primes up to n
    """
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)

    idx = 2
    while idx * idx <= n:
        if is_prime[idx]:
            for i in range(idx * 2, n + 1, idx):
                is_prime[i] = False
        idx += 1

    is_prime[0] = False
    is_prime[1] = False

    return sum(is_prime)


def permutation(n, rec):
    if n <= 1:
        return 1

    if rec[n] != -1:
        return rec[n]

    perm = n * permutation(n - 1, rec)
    return perm


def combination(n, i):
    """
    Compute C(n, i)
    """
    # Use rec to store the permutations we compute already.
    rec = [-1] * (n + 1)
    return int(permutation(n, rec) / permutation(i, rec) / permutation(n - i, rec))


def count_ways(n):
    """
     Count how many ways to cover the wall
    """
    # Typical combination
    # if n < 4, there is only one way to cover. There is 0 prime numbers smaller than 1
    if n < 4:
        return 0

    # first compute how many 4x1
    num_1x4_blocks = n // 4
    #print("num_4x1: {}".format(num_1x4_blocks))

    ret = 0
    for i in range(num_1x4_blocks + 1):
        # Each num_1x4_blocks is considered as 1 unit
        ret += combination(n - 4 * i + i, i)

    return ret


def redJohn(n):
    num_ways = count_ways(n)
    print("num_ways: {}".format(num_ways))
    return count_prime_sieve(num_ways)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
