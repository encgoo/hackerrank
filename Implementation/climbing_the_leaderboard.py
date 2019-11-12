#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbing Leaderboard function below.
def search_rank_rec(ranks, i, j, s):
    # print("searching {}->{}".format(i, j))
    if i == j:
        if ranks[i][0] == s:
            return ranks[i][1]
        elif ranks[i][0] > s:
            return ranks[i][1] + 1
        else:
            return ranks[i][1] - 1
    elif i + 1 == j:
        if ranks[j][0] == s:
            return ranks[j][1]
        elif s < ranks[j][0]:
            return ranks[j][1] + 1
        elif s >= ranks[i][0]:
            return ranks[i][1]
        else:
            return ranks[i][1] + 1
    else:
        middle = int((j - i) / 2) + i
        # print("middle: " + str(middle))
        if s == ranks[middle][0]:
            return ranks[middle][1]
        elif s < ranks[middle][0]:
            return search_rank_rec(ranks, middle, j, s)
        else:
            return search_rank_rec(ranks, i, middle - 1, s)


def climbingLeaderboard(scores, alice):
    ret = []

    ranks = []
    rank = 1
    last_score = scores[0]
    i = 0
    while i < len(scores):
        if scores[i] < last_score:
            ranks.append((last_score, rank))
            rank += 1
        last_score = scores[i]
        i += 1
    ranks.append((last_score, rank))
    print(ranks)

    for s in alice:
        if s > scores[0]:
            ret.append(1)
        elif s < ranks[-1][0]:
            ret.append(ranks[-1][1] + 1)
        elif s == ranks[-1][0]:
            ret.append(ranks[-1][1])
        else:
            # optimize
            rank = search_rank_rec(ranks, 0, len(ranks) - 1, s)
            ret.append(rank)

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
