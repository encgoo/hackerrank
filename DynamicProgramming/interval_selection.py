#!/bin/python3

import os
import sys


#
# Complete the intervalSelection function below.
#
def intervalSelection(intervals):
    # Key point: use the end as the first key, then the start
    intervals.sort(key=lambda u: (u[1], u[0]))

    print(intervals)

    result = 1
    cur_end = 1
    interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= cur_end:
            result += 1
            if interval[1] >= intervals[i][0]:
                cur_end = interval[1] + 1
            interval = intervals[i]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()
