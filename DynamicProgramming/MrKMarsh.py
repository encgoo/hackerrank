# https://www.hackerrank.com/challenges/mr-k-marsh/problem?isFullScreen=true
from collections import deque


def is_rect(rec, tx,ty, bx, by):
    hor_ok = rec[by][tx][0] + tx >= bx
    ver_ok = rec[ty][bx][1] + ty >= by
    return ver_ok and hor_ok

# bfs
def find_rect_big_to_small(rec, tx, ty, bx, by):
    q = deque()
    q.append((bx, by))

    while q:
        cor = q.popleft()
        if is_rect(rec, tx, ty, cor[0], cor[1]):
            # found rect
            return -tx - ty + cor[0] + cor[1]
        if cor[0] > tx + 1 and (cor[0] - 1, cor[1]) not in q:
            q.append((cor[0] - 1, cor[1]))
        if cor[1] > ty + 1 and (cor[0], cor[1] - 1) not in q:
            q.append((cor[0], cor[1] - 1))

    return 0


def find_largest(rec, tx, ty, lrg):
    # find the largest rect started from (tx, ty)
    if rec[ty][tx][0] == 0 or rec[ty][tx][1] == 0:
        # no way to make any rec
        return lrg
    # longest to reach
    bx = tx + rec[ty][tx][0]
    by = ty + rec[ty][tx][1]

    if bx - tx + by - ty <= lrg:
        return lrg

    # look for the largest recursively
    tmp = find_rect_big_to_small(rec, tx, ty, bx, by)
    return max(tmp, lrg)


def find_longest(grid):
    num_r = len(grid)
    num_c = len(grid[0])

    rec = [[(0, 0)]*num_c for _ in range(num_r)]

    col = num_c - 1
    row = num_r - 1

    if grid[row][col] == '.':
        rec[row][col] = (0, 0)
    else:
        rec[row][col] = (-1, -1)

    col = num_c - 2
    while col >= 0:
        if grid[row][col] == '.':
            rec[row][col] = (rec[row][col + 1][0] + 1, 0)
        else:
            rec[row][col] = (-1, -1)
        col -= 1

    row = num_r - 2
    while row >= 0:
        if grid[row][col] == '.':
            rec[row][col] = (0, rec[row + 1][col][1] + 1)
        else:
            rec[row][col] = (-1, -1)
        row -= 1

    row = num_r - 2
    while row >= 0:
        col = num_c - 2
        while col >= 0:
            if grid[row][col] == '.':
                rec[row][col] = (rec[row][col + 1][0] + 1, rec[row + 1][col][1] + 1)
            else:
                rec[row][col] = (-1, -1)

            col -= 1
        row -= 1

    lrg = 0

    for i in range(num_r):
        for j in range(num_c):
            lrg = find_largest(rec, j, i, lrg)

    return 2*lrg


if __name__ == '__main__':
    grid = ['.....',
            '.x...',
            '.x..x',
            '..x..']
    print(find_longest(grid))