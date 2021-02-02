# Baekjoon no.2580 스도쿠
# Keyword: Back tracking
import sys

finish = False


def solution(s):
    global finish
    global zeros
    if finish:
        return
    if s == len(zeros):
        finish = True
        for row in grid:
            print(' '.join(map(str, row)))
        return
    else:
        i, j = zeros[s]
        # if grid[i][j] > 0:
        #     continue
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
            if grid[(i // 3) * 3 + k // 3][(j // 3) * 3 + k % 3] in candidates:
                candidates.remove(grid[(i // 3) * 3 + k // 3][(j // 3) * 3 + k % 3])
        # search
        if len(candidates) != 0:
            for candidate in candidates:
                grid[i][j] = candidate
                solution(s + 1)
                grid[i][j] = 0

        return


grid = []
# zeros = set()
zeros = []
for _ in range(9):
    row = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    grid.append(row)

# Construct search list
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            zeros.append((i, j))
solution(0)