# Baekjoon no.9015
# Keyword: Geometry
import sys
T = int(sys.stdin.readline())


def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2


for _ in range(T):
    N = int(sys.stdin.readline())
    points = []
    mat = {}
    for __ in range(N):
        points.append(tuple(map(int, sys.stdin.readline().split(' '))))

    for i in range(N):
        p1 = points[i]
        for j in range(i, N):
            p2 = points[j]
            d = dist(p1, p2)
            if d not in mat:
                mat[d] = 1
            else:
                mat[d] += 1
    print(mat)
    candidates = list(filter(lambda x: x[1] >= 4, mat.items()))

    print(candidates)
    candidates = sorted(candidates, key=lambda x: x[0], reverse=True)
    print(candidates)
    print(candidates[0][0])