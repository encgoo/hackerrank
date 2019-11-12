#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
filled = None


def fill_words(words, iii, spaces, cur_filled):
    global filled
    if iii >= len(words):
        filled = cur_filled
        return

    word = words[iii]
    possible_spaces = [s for s in spaces if s[3] == len(word)]
    for s in possible_spaces:
        i = s[0]
        j = s[1]
        direction = s[2]
        good = True
        filled_tmp = [cur_filled[i][:] for i in range(len(cur_filled))]
        if direction == 1:
            for k in range(len(word)):
                row = list(filled_tmp[i])
                if filled_tmp[i][j + k] == '-' or filled_tmp[i][j + k] == word[k]:
                    row[j + k] = word[k]
                else:
                    good = False
                filled_tmp[i] = ''.join(row)

        elif direction == 2:
            for k in range(len(word)):
                if filled_tmp[i + k][j] == '-' or filled_tmp[i + k][j] == word[k]:
                    # filled_tmp[i + k][j] = word[k]
                    filled_tmp[i + k] = filled_tmp[i + k][:j] + word[k] + filled_tmp[i + k][j + 1:]
                else:
                    good = False
        if good:
            # print(word)
            # print(filled_tmp)
            fill_words(words, iii + 1, spaces, filled_tmp)


def crosswordPuzzle(crossword, words):
    spaces = []
    checked = [[0] * len(crossword[0]) for i in range(len(crossword))]

    for i in range(len(crossword)):
        for j in range(len(crossword[0])):
            if crossword[i][j] == '-':

                if checked[i][j] != 1 and checked[i][j] != 3:
                    tmp = j
                    while tmp < len(crossword[0]) and crossword[i][tmp] == '-':
                        # checked horizontal already
                        checked[i][tmp] += 1
                        tmp += 1

                    sz = tmp - j
                    if sz >= 2:
                        spaces.append((i, j, 1, sz))
                    else:
                        checked[i][j] -= 1

                if checked[i][j] != 3 and checked[i][j] != 2:
                    tmp = i
                    while tmp < len(crossword) and crossword[tmp][j] == '-':
                        checked[tmp][j] += 2
                        tmp += 1
                    sz = tmp - i
                    if sz >= 2:
                        spaces.append((i, j, 2, sz))
                    else:
                        checked[i][j] -= 2
    ws = words.split(';')
    fill_words(ws, 0, spaces, crossword)
    return filled


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
