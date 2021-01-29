# Baekjoon no.1744 수 묶기
# Keyword: Sorting, Greedy
import sys

n = int(sys.stdin.readline())
plus = []
minus = []
ones = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 1:
        ones.append(k)
    elif k > 0:
        plus.append(k)
    else:
        minus.append(k)

plus = sorted(plus, reverse=True)
minus = sorted(minus)

def calc(arr):
    print('-'*80)
    print(arr)
    res = 0
    if len(arr) < 2:
        res = sum(arr)
    else:
        for i in range(0, len(arr), 2):
            if i == len(arr) - 1:
                res += arr[i]
                break
            res += arr[i]*arr[i+1]
    print('1. ', res)
    return res
result = calc(plus) + calc(minus) + len(ones)
print(result)