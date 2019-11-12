#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
area = 0
def find_region_area(matrix, i, j, visited):
    global area
    if i < 0 or j < 0 or i >= len(matrix) or j >=len(matrix[0]):
        return
    if visited[i][j] or matrix[i][j] == 0:
        return
    visited[i][j] = True
    area += 1

    find_region_area(matrix, i - 1, j, visited)
    find_region_area(matrix, i - 1, j - 1, visited)
    find_region_area(matrix, i - 1, j + 1, visited)
    find_region_area(matrix, i, j - 1, visited)
    find_region_area(matrix, i, j + 1, visited)
    find_region_area(matrix, i + 1, j, visited)
    find_region_area(matrix, i + 1, j - 1, visited)
    find_region_area(matrix, i + 1, j + 1, visited)

def connectedCell(matrix):
    global area
    visited = [[False]*len(matrix[0]) for i in range(len(matrix))]
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                area = 0
                find_region_area(matrix, i, j, visited)
                if area > max_area:
                    max_area = area

    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
