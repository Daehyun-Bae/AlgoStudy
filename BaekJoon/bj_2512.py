# Baekjoon no.2512 예산

N = int(input())
req = list(map(int, input().split(' ')))
budget = int(input())


def calc_max(n, req, budget, q, i):
    for j in range(i-1, -1, -1):
        max_boundary = (budget - q[j]) // (n - j - 1)
        if max_boundary > req[j]:
            return max_boundary

    return budget // n


def solution(n, req, budget):
    req = sorted(req)
    acc = 0
    q = []

    for i, r in enumerate(req):
        acc += r
        q.append(acc)
        # Calc max boundary if cumulative sum is over budget
        if acc > budget:
            return calc_max(n, req, budget, q, i)

    return req[-1]


print(solution(N, req, budget))