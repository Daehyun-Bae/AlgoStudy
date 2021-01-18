# Baekjoon no.1915 가장 큰 정사각형

import sys


def solution(n, m, grid):
    answer = 0
    return answer


def show_grid(grid):
    for row in grid:
        print(row)


n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().rstrip()]
    grid.append(row)


show_grid(grid)
