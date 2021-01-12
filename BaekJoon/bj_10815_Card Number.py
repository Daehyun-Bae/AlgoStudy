# Baekjoon no.10815: 숫자 카드

import sys

def solution(n, n_list, m, m_list):
    answer = [0 for i in range(len(m_list))]

    for i, k in enumerate(m_list):
        if k in n_list:
            answer[i] = 1

    return answer

n = int(sys.stdin.readline())
n_list = sys.stdin.readline().rstrip().split(' ')
n_list = list(map(int, n_list))

m = int(sys.stdin.readline())
m_list = sys.stdin.readline().rstrip().split(' ')
m_list = list(map(int, m_list))

print(solution(n, n_list, m, m_list))

# cases = [[5, [6, 3, 2, 10, -10], 8, [10, 9, -5, 2, 3, 4, 5, -10]]]

# for case in cases:
#     a, b, c, d = case
#     print(solution(a, b, c, d))
