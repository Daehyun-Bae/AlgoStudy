import sys
from collections import deque

# U D L R
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(n, m, grid):
    hammer = 1
    visited = [[[0]*m for _ in range(n)] for __ in range(hammer+1)]
    q = deque([[[0, 0], hammer, 1]])

    while len(q) > 0:
        (cy, cx), hammer, move = q.pop()
        # Goal check
        if cy == n - 1 and cx == m - 1:
            return move

        if visited[hammer][cy][cx] == 1:
            continue

        for h in range(hammer+1):
            visited[h][cy][cx] = 1

        for i in range(4):
            if -1 < cy + dy[i] < n and -1 < cx + dx[i] < m:
                if grid[cy + dy[i]][cx + dx[i]] == 1:
                    if hammer > 0 and visited[hammer][cy + dy[i]][cx + dx[i]] == 0:
                        q.appendleft([[cy + dy[i], cx + dx[i]], hammer - 1, move + 1])
                else:
                    if visited[hammer][cy + dy[i]][cx + dx[i]] == 0:
                        q.appendleft([[cy + dy[i], cx + dx[i]], hammer, move + 1])

    return -1

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().rstrip()]
    grid.append(row)


print(solution(n, m, grid))