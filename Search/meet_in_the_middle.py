#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def find_zero_sum(l1, l2, l3, l4):
    """
    Brute force approach. Use 4 for-loops to find all the possibilities
    :return:
    """
    count = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            for k in range(len(l3)):
                for l in range(len(l4)):
                    if l1[i] + l2[j] + l3[k] + l4[l] == 0:
                        count += 1
    return count


def meet_in_the_middle(l1, l2, l3, l4):
    """
    Meet in the middle. Assume that we are looking for a+b+c+d =0. We can
    cache all the possible a+b results in the first for loop.

    :param lst:
    :return:
    """
    cache = {}

    for i in range(len(l1)):
        for j in range(len(l2)):
            d = l1[i] + l2[j]
            if d in cache:
                cache[d] += 1
            else:
                cache[d] = 1
    count = 0
    for i in range(len(l3)):
        for j in range(len(l4)):
            d = -l3[i] - l4[j]
            if d in cache:
                count += cache[d]

    return count


if __name__ == "__main__":
    l1 = [2, 3, 1, 0, -4, 1]
    l2 = [-2, 3, 1, 0, -4, -1]
    l3 = [2, -1, 1, 0, -4, 1]
    l4 = [5, 3, 4, 0, -4, -1]

    t0 = time.time()
    ret = find_zero_sum(l1, l2, l3, l4)
    print("{}, {}".format(ret, time.time() - t0))
    t0 = time.time()
    ret = meet_in_the_middle(l1, l2, l3, l4)
    print("{}, {}".format(ret, time.time() - t0))