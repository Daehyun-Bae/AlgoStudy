# Baekjoon no.9663 N-Queen
# Keyword: Back tracking
import time
n = int(input())
count = 0
col, diag_l, diag_r = set(), set(), set()


def dfs(r, grid):
    global count
    if r == n:
        count += 1
        return 0
    else:
        candidates = list(range(n))
        for k in range(r):
            if grid[k] in candidates:
                candidates.remove(grid[k])

            cross_pt_l = grid[k] - (r - k)
            cross_pt_r = grid[k] + (r - k)
            if cross_pt_l in candidates:
                candidates.remove(cross_pt_l)
            if cross_pt_r in candidates:
                candidates.remove(cross_pt_r)

        for candidate_pt in candidates:
            grid.append(candidate_pt)
            dfs(r + 1, grid)
            grid.remove(candidate_pt)


def dfs2(r, col, diag_l, diag_r):
    global count
    if r == n:
        count += 1
        return 0
    else:
        # i-th column check
        for i in range(n):
            if i in col or i - r in diag_l or i + r in diag_r:
                continue
            col.add(i)
            diag_l.add(i - r)
            diag_r.add(i + r)
            dfs2(r + 1, col, diag_l, diag_r)
            col.remove(i)
            diag_l.remove(i - r)
            diag_r.remove(i + r)


s = time.time()
dfs(0, [])
print(count)
print(f'{time.time() - s:.4f}')


s = time.time()
count = 0
dfs2(0, col, diag_l, diag_r)
print(count)
print(f'{time.time() - s:.4f}')
