# Baekjoon no.11053 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int, input().split(' ')))


def solution(n, arr):
    MAX = 0
    answer = 0
    for a in arr:
        if MAX < a:
            MAX = a
            answer += 1

    return answer


print(solution(n, arr))