# Baekjoon no.1915 가장 큰 정사각형

import sys


def solution(n, m, grid):
    memo = [[0] * m for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if memo[i-1][j-1] > 0 and memo[i-1][j] > 0 and memo[i][j-1] > 0:
                    memo[i][j] = min([memo[i-1][j-1], memo[i-1][j], memo[i][j-1]]) + 1
                    show_grid(memo)
                else:
                    memo[i][j] = 1
                answer = max(answer, memo[i][j])
    return answer * answer


def show_grid(grid):
    for row in grid:
        print(row)
    print('-' * 80)


n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().rstrip()]
    grid.append(row)


show_grid(grid)
print(solution(n, m, grid))