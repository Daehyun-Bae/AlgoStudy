# Baekjoon no.3830 교수님은 기다리지 않는다.
from collections import deque
END = '0 0'
output = ''


class union_fnd:
    def __init__(self, n):
        # Root node of i-th node
        self.root = [i for i in range(n + 1)]
        # Height of tree containing i
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.root[x] == x:
            # print("TRUE")
            return x
        else:
            return self.find(self.root[x])
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        self.root[root_x] = root_y
        # print(self.root)


def bfs(data, graph, start, goal):
    q = deque([(start, [start], [0] * len(graph))])
    
    while len(q) > 0:
        cur, path, visited = q.pop()
        if cur == goal:
            return path
        
        if visited[cur] == 1:
            continue
        else:
            visited[cur] = 1
        adj = data[cur]
        for a in adj:
            q.append((a, path + [a], visited))

    return -1   # Fail to find path


while True:
    test = input()
    if test == END:
        # print('---END---')
        break
    n_sample, n_case = map(int, test.split())
    db = union_fnd(n=n_sample)
    # data = {}   # store adjacency node info
    graph = [[0] * (n_sample + 1) for _ in range(n_sample + 1)]

    for c in range(n_case):
        command = input().split()
        if command[0] == '!':
            a, b, w = map(int, command[1:])
            # if a not in data:
            #     data[a] = [b]
            # else:
            #     data[a].append(b)           
            
            # if b not in data:
            #     data[b] = [a] 
            # else:
            #     data[b].append(a)
            db.union(a, b)
            graph[a][b] = w
            graph[b][a] = -w

            # print(data)
            # show_graph(graph)
        if command[0] == '?':
            a, b = map(int, command[1:])
            root_a = db.find(a)
            root_b = db.find(b)
            if root_a != root_b:
                output += 'UNKNOWN\n'
            else:
                cost = 0
                cnt = 0
                while a != root_a:
                    cost += graph[a][db.root[a]]
                    print(f'[{a}] -> [{db.root[a]}] ({cost})')
                    a = db.root[a]
                    cnt += 1
                    if cnt == 10:
                        break
                while b != root_b:
                    cost -= graph[b][db.root[b]]
                    print(f'[{b}] -> [{db.root[b]}] ({cost})')
                    b = db.root[b]
                    cnt += 1
                    if cnt == 10:
                        break
                
                output += '{}\n'.format(cost)
            # if a not in data or b not in data:
            #     output += 'UNKNOWN\n'
            # else:
            #     path = bfs(data=data, graph=graph, start=a, goal=b)
            #     if path == -1:
            #         output += 'UNKNOWN\n'
            #     else:
            #         cost = 0
            #         for i in range(len(path)-1):
            #             cost += graph[path[i]][path[i+1]]
            #         output += '{}\n'.format(cost)    
    # print('next case')
print(output)