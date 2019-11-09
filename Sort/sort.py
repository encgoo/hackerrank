#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


def selection_sort(l):
    # in place sort
    for i in range(len(l)):
        min_v = l[i]
        index_v = -1
        for j in range(i + 1, len(l)):
            if l[j] < min_v:
                min_v = l[j]
                index_v = j
        # swap
        if index_v != -1:
            l[i], l[index_v] = l[index_v], l[i]


def bubble_sort(l):
    # also in place sort
    for i in range(len(l)):
        for j in range(i, len(l) - 1 - i):
            if l[j] > l[j + 1]:
                # swap
                l[j], l[j + 1] = l[j + 1], l[j]
#
#   Merge sort
#
def merge(l, i, j, m):
    ll = l[i: j + 1]
    rl = l[j+1: m + 1]

    l_p = 0
    r_p = 0
    w_p = i

    while l_p < len(ll) and r_p < len(rl):
        if ll[l_p] < rl[r_p]:
            l[w_p] = ll[l_p]
            w_p += 1
            l_p += 1
        else:
            l[w_p] = rl[r_p]
            w_p += 1
            r_p += 1
    # copy whatever left in ll, if there is any
    while l_p < len(ll):
        l[w_p] = ll[l_p]
        l_p += 1
        w_p += 1
    # copy whatever left in rl, if there is any
    while r_p < len(rl):
        l[w_p] = rl[r_p]
        r_p += 1
        w_p +=1


def merge_sort_rec(l, i, j):
    # recursive, need to stop
    # think about the bottom case i + 1 = j. Stop here, not i == j case
    if i + 1 == j:
        if l[i] > l[j]:
            # swap
            l[i], l[j] = l[j], l[i]
        # Done
        return
    if i == j:
        # if three left, when split, first half has two the second half has one
        return

    # note if j = i + 1, this will be zero, so better stop the
    # recursive process for j = i + 1
    middle = int((j - i)/2) + i

    # split into two
    merge_sort_rec(l, i, middle)
    merge_sort_rec(l, middle + 1, j)
    merge(l, i, middle, j)

#
# Quick sort
#
def partition(l, i, j):
    pivot_v = l[i]
    pivot_p = i

    for ii in range(i + 1, j + 1):
        if l[ii] < pivot_v:
            # increment pivot_p first
            # this makes sure pivot_p is always
            # pointing at the last one smaller than
            # pivot_v
            pivot_p += 1
            #swap
            l[ii], l[pivot_p] = l[pivot_p], l[ii]

    # swap i and pivot_p
    l[i], l[pivot_p] = l[pivot_p], l[i]

    return pivot_p


def quick_sort_rec(l, i, j):
    if i >= j:
        # can't partition any more. Nothing else to do
        return

    pat = partition(l, i, j)
    quick_sort_rec(l, i, pat - 1)
    quick_sort_rec(l, pat + 1, j)

if __name__ == "__main__":
    l = [1, 0, 2, 9, 3, 8, 4, 8, 5, 7, 6, 100, 90, 80, 70, 60, 50, 40,30, 20]
    print(l)
    print("selection sort: ")
    tmp = l[:]
    t0 = time.time()
    selection_sort(tmp)
    print("{}, {}".format(time.time() - t0, tmp))

    print("bubble sort:")
    tmp = l[:]
    t0 = time.time()
    bubble_sort(tmp)
    print("{}, {}".format(time.time() - t0, tmp))

    print("merge sort:")
    tmp = l[:]
    t0 = time.time()
    merge_sort_rec(tmp, 0, len(tmp) - 1)
    print("{}, {}".format(time.time() - t0, tmp))

    print("quick sort:")
    tmp = l[:]
    t0 = time.time()
    quick_sort_rec(tmp, 0, len(tmp) - 1)
    print("{}, {}".format(time.time() - t0, tmp))

