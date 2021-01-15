# Baekjoon no.2267 단지 번호
# Category: BFS

import sys
from collections import deque

# U D L R
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(n, grid):
    group = {}
    num_g = 1
    visited = [[0]*n for _ in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1 or grid[i][j] == 0:
                continue
            
            if len(q) == 0:
                q.appendleft([i, j])
            
            while len(q) > 0:
                (cy, cx) = q.pop()
                if visited[cy][cx] == 1:
                    continue
                visited[cy][cx] = 1

                if grid[cy][cx] == 1:
                    if num_g not in group:
                        group[num_g] = 1
                    else:
                        group[num_g] += 1
                
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if -1 < ny < n and -1 < nx < n:
                        if grid[ny][nx] == 1:
                            q.appendleft([ny, nx])
                        else:
                            visited[ny][nx] = 1
            
            num_g += 1

    print(len(group))
    group_list = sorted([item[1] for item in group.items()])
    for n in group_list:
        print(n)

n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    row = [int(x) for x in sys.stdin.readline().rstrip()]
    grid.append(row)

solution(n, grid)