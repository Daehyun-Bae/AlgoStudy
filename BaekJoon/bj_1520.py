# Baekjoon no.1991 트리순회
# Keyword: Dynamic Programming
import sys

m, n = map(int, sys.stdin.readline().split())
grid = []
visited = [[0] * n for _ in range(m)]
memo = [[0] * n for _ in range(m)]
for _ in range(m):
    grid.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))


def chk_adj(i, j):
    cnt = 0
    if not visited[i][j]:
        visited[i][j] = 1
        cur_h = grid[i][j]
        # upper
        if i > 0:
            if grid[i - 1][j] > cur_h:
                cnt += chk_adj(i - 1, j)

        # lower
        if i < m - 1:
            if grid[i + 1][j] > cur_h:
                cnt += chk_adj(i + 1, j)

        # left
        if j > 0:
            if grid[i][j - 1] > cur_h:
                cnt += chk_adj(i, j - 1)

        # right
        if j < n - 1:
            if grid[i][j + 1] > cur_h:
                cnt += chk_adj(i, j + 1)
        memo[i][j] = cnt
        return cnt
    else:
        return memo[i][j]

visited[0][0] = 1
memo[0][0] = 1

# for i in range(m):
#     for j in range(n):
#         if visited[i][j]:
#             continue
#         chk_adj(i, j)
chk_adj(0, 0)
print(memo[m-1][n-1])