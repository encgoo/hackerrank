#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def make_one_move(lst, i, j):
    #if (i + 1) not in lst:
        # Nothing to move from i to j
    #    return None

    # find the highest disc of i rod
    tmp = 0
    top_i = -1
    top_j = -1
    found_i = False
    found_j = False
    while tmp < len(lst) and not (found_i and found_j):
        if lst[tmp] == i + 1 and not found_i:
            top_i = tmp
            found_i = True
        if lst[tmp] == j + 1 and not found_j:
            top_j = tmp
            found_j = True
        tmp += 1
    if top_i == -1:
        # nothing on rod i to move
        return None

    if top_i > top_j and top_j != -1:
        # Can't move
        return None
    ret = lst[:]
    ret[top_i] = j + 1
    #print ("i {}, j {}, top_i {}, top_j {}, {}->{}".format(i, j, top_i, top_j, lst, ret))
    return ret
def lst_to_index(lst):
    ret = 0
    for i in lst:
        ret = ret << 2 | (i - 1)
    return ret

def find_steps(N, a):
    # BFS
    visited = [False]*(4**N)
    q = deque([a])
    visited[lst_to_index(a)] = True
    min_count = 0
    done = False
    while len(q) > 0 and not done:
        min_count += 1
        sz = len(q)
        #print("len of q: {}, sz: {}".format(sz, sys.getsizeof(q)))
        for _ in range(sz):
            lst = q.popleft()
            #visited[lst_to_index(lst)] = True
            for i in range(4):
                for j in range(4):
                    if i != j:
                        ret = make_one_move(lst, i, j)
                        if ret is not None:
                            # Check if we are done here
                            if sum(ret) == N:
                                #print("found {}".format(ret))
                                done = True
                                break
                            index = lst_to_index(ret)
                            if visited[index] is False:
                                q.append(ret)
                                visited[index] = True
                if done:
                    break
            if done:
                break
    print(min_count)
    return

if __name__ == '__main__':
    N = int(input())

    a = list(map(int, input().rstrip().split()))

    find_steps(N, a)
