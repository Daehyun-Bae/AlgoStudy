# Baekjoon no.2839 설탕배달
# Category: Dynamic programming
import sys
from itertools import combinations, permutations, product


def solution(N):
    memo = {3: 1, 5: 1}  # Initialize

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

# N = int(sys.stdin.readline())

cases = [3, 18, 4, 6, 9, 11, 27, 500, 5000]

for case in cases:
    print(solution(case))
    print('-'*40)