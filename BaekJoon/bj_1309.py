# Baekjoon no.1395 동물원

N = int(input())


def solution(n):
    memo = [3, 7]
    if n < 3:
        return memo[n-1]
    for i in range(n-2):
        memo.append(memo[-1] * 2 + memo[-2])
        del memo[0]
    return memo[-1] % 9901

for i in range(1, 15):
    print(solution(i))