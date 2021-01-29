# Baekjoon no.1260 DFS와 BFS
# Keyword: BFS, DFS
import sys
from collections import deque


n, m, root = map(int, sys.stdin.readline().rstrip('\n').split())
adj = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)


def bfs(root):
    visited = [0 for _ in range(n+1)]
    q = deque([root])
    path = []
    while len(q) > 0:
        cur = q.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        path.append(cur)
        adj_nodes = adj[cur]
        for node in sorted(adj_nodes):
            q.appendleft(node)
    return path


def dfs(root):
    visited = [0 for _ in range(n+1)]
    s = deque([root])
    path = []
    while len(s) > 0:
        cur = s.pop()
        if visited[cur]:
            continue
        visited[cur] = 1
        path.append(cur)
        adj_nodes = adj[cur]
        for node in sorted(adj_nodes, reverse=True):
            s.append(node)
    return path

print(' '.join(map(str, dfs(root))))
print(' '.join(map(str, bfs(root))))
