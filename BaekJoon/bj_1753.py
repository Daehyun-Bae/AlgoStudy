# Baekjoon no.1753 최단경로
# Keyword: Graph
import sys
import heapq

V, E = map(int, sys.stdin.readline().split(' '))
start = int(sys.stdin.readline())

nn = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split(' '))
    nn[s].append((e, w))


# initialize
d = {}
d[start] = 0

for i in range(1, V+1):
    if i != start:
        d[i] = float('inf')
q = []
visited = [0 for _ in range(V+1)]

heapq.heappush(q, (d[start], start))
while len(q) > 0:
    cur_dist, cur_node = heapq.heappop(q)
    if visited[cur_node]:
        continue
    visited[cur_node] = 1

    for next_node, weight in nn[cur_node]:
        new_dist = d[cur_node] + weight
        if new_dist < d[next_node]:
            d[next_node] = new_dist
            heapq.heappush(q, (d[next_node], next_node))


for i, v in sorted(d.items(), key=lambda x: x[0]):
    print(v if v != float('inf') else 'INF')


