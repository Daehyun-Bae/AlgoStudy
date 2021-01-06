# Baekjoon no.2839 설탕배달
# Category: Dynamic programming
import sys
from itertools import combinations, permutations, product


def solution(N):
    # memo = {1: [3, 5]}  # Initialize
    memo = {3: 1, 5: 1}  # Initialize
    i = 2
    print(f'N: {N}')
    if N in memo:
        return memo[N]
    while True:
        results = []
        for a, b in product(memo.keys(), memo.keys()):
            s = a + b
            if s > N:
                continue

            if s == N:
                return memo[a] + memo[b]

            if s not in memo:
                memo[s] = memo[a] + memo[b]
                results.append(s)

        if not results:
            return -1

        #
        # results = []
        # for j in range(1, i//2 + 1):
        #     print(j)
        #     # arr1 = memo[j]
        #     arr1 = filter(lambda x: memo[x] == j, memo.keys())
        #     # arr2 = memo[i - j]
        #     arr2 = filter(lambda x: memo[x] == i - j, memo.keys())
        #     sub_result = set(map(lambda x: x[0] + x[1], product(arr1, arr2)))
        #     sub_result = list(filter(lambda x: x <= N, sub_result))
        #     if N in sub_result:
        #         return i
        #     for k in sub_result:
        #         if k not in memo:
        #             memo[k] = i
        #     results += sub_result
        # if not results:
        #     return -1
        #
        # # memo[i] = results
        # i += 1


# N = int(sys.stdin.readline())

cases = [3, 18, 4, 6, 9, 11, 27, 500, 5000]

for case in cases:
    print(solution(case))
    print('-'*40)