# Baekjoon no.3830 교수님은 기다리지 않는다.
# Keyword: union-find
import sys
sys.setrecursionlimit(10**5)
output = ''


# 0: Root node of i-th node
# 1: Cost from i-th node to root node
# 2: Set size
# root = [[i, 0, 0] for i in range(100001)]


def find(x):
    if root[x][0] == x:
        return x
    else:
        root_x = find(root[x][0])
        root[x][1] += root[root[x][0]][1]
        root[x][0] = root_x
        return root_x

def union(x, y, w):
    root_x = root[x][0]
    root_y = root[y][0]
    # Attach smaller set to larger one
    if root_x != root_y:
        if root[x][2] <= root[y][2]:
            root[root_x][0] = root_y
            root[root_x][1] += root[y][1] - root[x][1] + w
            root[root_y][2] += root[root_x][2]
            root[root_x][2] = 1
        else:
            root[root_y][0] = root_x
            root[root_y][1] -= root[y][1] - root[x][1] + w
            root[root_x][2] += root[root_y][2]
            root[root_y][2] = 1

while True:
    test = sys.stdin.readline()
    n_sample, n_case = map(int, test.split())
    if n_sample == 0 and n_case == 0:
        break
    root = [[i, 0, 0] for i in range(n_sample + 1)]
    for c in range(n_case):
        command = sys.stdin.readline().split()
        a = int(command[1])
        b = int(command[2])
        root_a = find(a)
        root_b = find(b)
        if command[0] == '!':
            a, b, w = map(int, command[1:])
            union(a, b, w)
        elif command[0] == '?':
            a, b = map(int, command[1:])
            root_a = root[a][0]
            root_b = root[b][0]
            if root_a != root_b:
                output += 'UNKNOWN\n'
            else:
                cost = root[a][1] - root[b][1]               
                output += '{}\n'.format(cost)


print(output)