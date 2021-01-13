# Baekjoon no.1012 토마토

import sys
from collections import deque


def chk_tomato(today_bin, grid):
    next_bin = []
    new_tomato = 0
    while len(today_bin) > 0:
        show_grid(grid)
        print('-' * 80)
        cur_r, cur_c = today_bin.pop()

        # check adjacent cells
        # up
        if cur_r > 0 and grid[cur_r - 1][cur_c] == 0:
            grid[cur_r - 1][cur_c] = 1
            new_tomato += 1
            next_bin.append([cur_r - 1, cur_c])

        # down
        if cur_r < n - 1 and grid[cur_r + 1][cur_c] == 0:
            grid[cur_r + 1][cur_c] = 1
            new_tomato += 1
            next_bin.append([cur_r + 1, cur_c])

        # left
        if cur_c > 0 and grid[cur_r][cur_c - 1] == 0:
            grid[cur_r][cur_c - 1] = 1
            new_tomato += 1
            next_bin.append([cur_r,  cur_c - 1])

        # right
        if cur_c < m - 1 and grid[cur_r][cur_c + 1] == 0:
            grid[cur_r][cur_c + 1] = 1
            new_tomato += 1
            next_bin.append([cur_r, cur_c + 1])

    return next_bin, new_tomato


def solution(m, n, grid):
    day = 0
    init_loc = []
    num_wall = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                init_loc.append([i, j])
            elif grid[i][j] == -1:
                num_wall += 1
    num_tomato = len(init_loc)
    today_bin = deque(init_loc)
    print('=' * 80)

    while len(today_bin) > 0:
        print(f"Day - {day}")
        next_bin, new_tomato = chk_tomato(today_bin, grid)
        num_tomato += new_tomato

        # check next_bin
        if len(next_bin) == 0:
            if num_tomato + num_wall < m * n:
                return -1
            return day
        else:
            show_grid(grid)
            print('='*80)
            today_bin = deque(next_bin)
            day += 1

    return day


def show_grid(grid):
    for row in grid:
        print(row)

m, n = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


show_grid(grid)
print(solution(m, n, grid))