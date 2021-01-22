# Baekjoon no.11725 트리의 부모 찾기
# Keyword: tree
from collections import deque
import sys

n_node = int(sys.stdin.readline())
memo = {i: [] for i in range(1, n_node+1)}
for n in range(n_node - 1):
    a, b = map(int, sys.stdin.readline().split())
    memo[a].append(b)
    memo[b].append(a)

# start from 1
q = deque([1])
visited = [0] * (n_node + 1)
parent = [0] * (n_node + 1)
while len(q) > 0:
    n = q.pop()
    if visited[n]:
        continue
    visited[n] = 1
    for adj in memo[n]:
        if not visited[adj]:
            parent[adj] = n
            memo[adj].remove(n)
            q.appendleft(adj)

print('-'*80)
for n in range(2, n_node+1):
    print(f'{parent[n]}')
