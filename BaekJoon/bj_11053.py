# Baekjoon no.11053 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int, input().split(' ')))


def solution(n, arr):
    memo = [0 for _ in range(1001)]
    # start <= end <= Max
    L = []
    for a in arr:
        memo[a] = max(memo[:a]) + 1
        # memo.append(L)
        L.append(memo[a])
        print(f'[{a}] \t{L}')
    return max(L)

print(solution(n, arr))