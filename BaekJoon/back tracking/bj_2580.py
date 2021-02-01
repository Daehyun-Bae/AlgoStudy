# Baekjoon no.2580 스도쿠
# Keyword: Back tracking
import sys


def show_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def solution(start):
    if start == 81:
        print('-' * 80)

        for row in grid:
            print(' '.join(map(str, row)))        
        return 0
    # for i in range(r, 9):
    #     for j in range(c, 9):
    for s in range(81):
        i = s // 9
        j = s % 9
        if grid[i][j] > 0:
            continue
        # construct candidates
        candidates = [k for k in range(1, 10)]

        # check possible numbers
        for k in range(9):
            # row
            if grid[i][k] in candidates:
                candidates.remove(grid[i][k])
            # column
            if grid[k][j] in candidates:
                candidates.remove(grid[k][j])
            # 3x3 cell
            if grid[(i//3) * 3 + k//3][(j//3) * 3 + k%3] in candidates:
                candidates.remove(grid[(i//3) * 3 + k//3][(j//3) * 3 + k%3])
        show_grid(grid)
        # search
        if len(candidates) != 0:
            for candidate in candidates:
                grid[i][j] = candidate
                solution(s+1)

grid = []
for _ in range(9):
    row = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    grid.append(row)

solution(0)
# print('-' * 80)
# show_grid(grid)