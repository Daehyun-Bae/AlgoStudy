from collections import deque
END = '0 0'
output = ''


# Root node of i-th node
root = [[i, 0] for i in range(100001)]


def find(x, w):
    if root[x][0] == x:
        return x, w
    else:
        w -= root[x][1]
        return find(root[x][0], w)

def union(x, y, w):
    root_x = find(x, w)
    root_y = find(y, w)

    root[root_x][0] = root_y
    root[root_x][1] = 

while True:
    test = input()
    if test == END:
        break
    n_sample, n_case = map(int, test.split())
    graph = [[0] * (n_sample + 1) for _ in range(n_sample + 1)]

    for c in range(n_case):
        command = input().split()
        if command[0] == '!':
            a, b, w = map(int, command[1:])
            union(a, b)
            graph[a][b] = w
            graph[b][a] = -w

        if command[0] == '?':
            a, b = map(int, command[1:])
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                output += 'UNKNOWN\n'
            else:
                cost = 0
                while a != root_a:
                    cost += graph[a][root[a]]
                    a = root[a]
                    
                while b != root_b:
                    cost -= graph[b][root[b]]
                    b = root[b]
                
                output += '{}\n'.format(cost)
    # Init
    root = [i for i in range(100001)]


print(output)