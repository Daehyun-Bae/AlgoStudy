# Baekjoon no.1991 트리순회
# Keyword: Tree
import sys

N = int(sys.stdin.readline().rstrip('\n'))
node2num = {chr(ord('A')+i): i for i in range(N)}
num2node = list(node2num.keys())
tree = [[0, -1, -1] for _ in range(N)]


def get_left(t, n):
    return t[n][1]


def get_right(t, n):
    return t[n][2]


def preorder(t, n):
    if n >= 0:
        print(num2node[n], end='')
        preorder(t, get_left(t, n))
        preorder(t, get_right(t, n))


def inorder(t, n):
    if n >= 0:
        inorder(t, get_left(t, n))
        print(num2node[n], end='')
        inorder(t, get_right(t, n))


def postorder(t, n):
    if n >= 0:
        postorder(t, get_left(t, n))
        postorder(t, get_right(t, n))
        print(num2node[n], end='')


for _ in range(N):
    p, l, r = sys.stdin.readline().rstrip('\n').split()
    p = node2num[p]
    if l != '.':
        l = node2num[l]
        tree[p][1] = l
        tree[l][0] = p
    if r != '.':
        r = node2num[r]
        tree[p][2] = r
        tree[r][0] = p


preorder(t=tree, n=0)
print()
inorder(t=tree, n=0)
print()
postorder(t=tree, n=0)