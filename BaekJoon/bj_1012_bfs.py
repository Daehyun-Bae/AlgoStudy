# Baekjoon no.1012 유기농 배추
# Category: DFS, BFS
import sys
from queue import LifoQueue


def solution(m, n, k, coords):
    answer = 0
    if k == 1:
        return 1
    coords = sorted(coords, key=lambda x: x[0])
    grid = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for c in coords:
        grid[c[0]][c[1]] = 1

    stack = LifoQueue()

    for coord in coords:
        cx, cy = coord

        if visited[cx][cy] == 1:
            continue

        if stack.qsize() == 0:
            stack.put(coord)

        while stack.qsize() > 0:
            last_loc = stack.get()
            lx, ly = last_loc
            visited[lx][ly] = 1
            # right
            if ly < n - 1 and visited[lx][ly + 1] == 0:
                if grid[lx][ly + 1] == 1:
                    stack.put([lx, ly + 1])

            # left
            if ly > 0 and visited[lx][ly - 1] == 0:
                if grid[lx][ly - 1] == 1:
                    stack.put([lx, ly - 1])

            # down
            if lx < m - 1 and visited[lx + 1][ly] == 0:
                if grid[lx + 1][ly] == 1:
                    stack.put([lx + 1, ly])

            # up
            if lx > 0 and visited[lx - 1][ly] == 0:
                if grid[lx - 1][ly] == 1:
                    stack.put([lx - 1, ly])
        answer += 1

    # for g in grid:
    #     print(g)
    # print('-'*20)
    # for v in visited:
    #     print(v)
    return answer

'''
T = int(sys.stdin.readline())
answers = []
cases = []
for t in range(T):
    m, n, k = list(map(int, sys.stdin.readline().split(' ')))
    coord = []
    for i in range(k):
        coord.append(list(map(int, sys.stdin.readline().split(' '))))
    cases.append([m, n, k, coord])

for case in cases:
    m, n, k, coord = case
    answers.append(solution(m, n, k, coord))

for ans in answers:
    print(ans)
'''

cases = [[10, 8, 17, [[0, 0], [1, 0], [1, 1], [4, 2],
                      [4, 3], [4, 5], [2, 4], [3, 4],
                      [7, 4], [8, 4], [9, 4], [7, 5],
                      [8, 5], [9, 5], [7, 6], [8, 6], [9, 6]]],
         [10, 10, 1, [[5, 5]]],
         [5, 3, 6, [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 0]]],
         [5, 5, 12, [[3, 1], [1, 3], [0, 4],
                     [1, 4], [2, 4], [3, 4], [2, 2],
                     [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], ]],
         [5, 5, 5, [[0, 2], [1, 1], [1, 3], [1,2],
                     [2, 0],[2,2], [2, 4]]]
         ]

for case in cases:
    m, n, k, coord = case
    print(solution(m, n, k, coord))
    print('-'*100)