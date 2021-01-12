# Baekjoon no.10815: 숫자 카드
# Category: Binary search

import sys


def bin_search(arr, n):
    len_arr = len(arr)
    start = 0
    end = len_arr - 1
    k = (start + end) // 2

    while True:
        if arr[k] == n:
            return True
        if arr[k] > n:
            end = k
            k = (start + end) // 2
            if end == k:
                if arr[k] == n or arr[k-1] == n:
                    return True
                return False
        elif arr[k] < n:
            start = k
            k = (start + end) // 2
            if start == k:
                if arr[k] == n or arr[k + 1] == n:
                    return True
                return False


def solution(n, n_list, m, m_list):
    answer = ['0' for i in range(m)]
    n_list = sorted(n_list)
    for i, k in enumerate(m_list):
        if bin_search(n_list, k):
            answer[i] = '1'

    answer = ' '.join(answer)
    return answer


# n = int(sys.stdin.readline())
# n_list = sys.stdin.readline().rstrip().split(' ')
# n_list = list(map(int, n_list))
#
# m = int(sys.stdin.readline())
# m_list = sys.stdin.readline().rstrip().split(' ')
# m_list = list(map(int, m_list))
#
# print(solution(n, n_list, m, m_list))


cases = [[5, [6, 3, 2, 10, -10], 8, [10, 9, -5, 2, 3, 4, 5, -10]]]

for case in cases:
    a, b, c, d = case
    print(solution(a, b, c, d))
