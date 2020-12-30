# Baekjoon no.2143

import sys
from functools import reduce
from collections import Counter
from itertools import product


def acc_func(acc, cur):
    i, v = cur
    if i == 0:
        acc.append(v)
    else:
        acc.append(acc[i-1]+v)
    return acc


def solution(T, n, arr1, m, arr2):
    acc1 = []
    for i in range(n):
        acc1 += reduce(acc_func, enumerate(arr1[i:]), [])

    acc1_dict = dict(Counter(acc1))
    print(acc1)
    # acc1 = list(filter(lambda x: x < T, acc1))
    print(acc1)

    acc2 = []
    for i in range(m):
        acc2 += reduce(acc_func, enumerate(arr2[i:]), [])
    # acc2 = list(filter(lambda x: x < T, acc2))
    print(acc2)
    acc2_dict = dict(Counter(acc2))

    answer = 0

    for i in acc1_dict:
        if T - i in acc2_dict:
            answer += acc1_dict[i] * acc2_dict[T - i]

    # Time over
    # acc1_sub_sum = list(sorted(acc1_dict, reverse=T < 0))
    # acc2_sub_sum = list(sorted(acc2_dict, reverse=T < 0))
    # for i in acc1_sub_sum:
    #     for j in acc2_sub_sum:
    #         sub_sum = i + j
    #         if sub_sum == T:
    #             answer += acc1_dict[i] * acc2_dict[j]
    #         elif 0 < T < sub_sum or sub_sum < T < 0:
    #             break

    return answer

# stdin
# t = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
# a1 = sys.stdin.readline().rstrip().split()
# a1 = list(map(int, a1))
# m = int(sys.stdin.readline())
# a2 = sys.stdin.readline().rstrip().split()
# a2 = list(map(int, a2))
# print(solution(t, n, a1, m, a2))


cases = [[5, 4, [1, 3, 1, 2], 3, [1, 3, 2]]]

for case in cases:
    t, n, a1, m, a2 = case
    print(solution(t, n, a1, m, a2))