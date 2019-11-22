#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    total = n * m
    space_left = total

    row_tracks = {}

    for t in track:
        if t[0] - 1 in row_tracks:
            row_tracks[t[0] - 1].append((t[1], t[2]))
        else:
            row_tracks[t[0] - 1] = [(t[1], t[2])]

    for r in row_tracks.keys():
        tracks = row_tracks[r]
        track_line = []
        for t in tracks:
            s = t[0] - 1
            e = t[1] - 1
            track_line.append((s, 1))
            track_line.append((e, -1))
        track_line.sort(key=lambda t: (t[0], -t[1]))
        ts = 0
        # the first one must be a start
        pre_loc = -1
        print(track_line)
        print(space_left)
        for b in track_line:
            print("ts {}, space_left {}".format(ts, space_left))
            handled = False
            if b[1] == 1:
                # start of a track
                ts += 1
                if ts == 1 and b[0] != pre_loc:
                    # corner case
                    space_left -= 1
                    handled = True

            if ts > 0 and not handled:
                space_left -= b[0] - pre_loc

            if b[1] == -1:
                ts -= 1
            pre_loc = b[0]

    return space_left


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
