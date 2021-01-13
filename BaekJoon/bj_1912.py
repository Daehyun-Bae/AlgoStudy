# Baekjoon no.1912 연속합


def solution(arr):
    best = arr[0]
    cumulative = 0
    for v in arr:
        cumulative += v
        best = cumulative if cumulative > best else best
        cumulative = cumulative if cumulative < 0 else 0

    return best


def solution2(arr):
    cumulative = before_best = prev = arr[0]
    for cur in arr[1:]:
        cumulative = max(prev, cumulative) + cur
        before_best = max([cumulative, before_best, prev])
        prev = cur

    return max([cumulative, before_best, prev])


# n = int(input())
# arr = list(map(int, input().split()))
# print(solution(n, arr))


cases = [[10, [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]],
         [10, [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]],
         [5, [-1, -2, -3, -4, -5]],
         [5, [31, -20, -50, 20, 30]]]

for n, arr in cases:
    print(solution(arr))
    print('-' * 50)
