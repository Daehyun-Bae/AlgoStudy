# Baekjoon no.9184 신나는 함수 실행
# Keyword: Dynamic Programming
import sys
memo = [[[0] * 21 for _ in range(21)] for __ in range(21)]


def func(a, b, c):
    # print(f'({a}, {b}, {c})')
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)

    if memo[a][b][c] != 0:
        return memo[a][b][c]

    if a < b < c:
        memo[a][b][c] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)

    else:
        memo[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)

    return memo[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().rstrip('\n').split())
    if a == -1 and b == -1 and c == -1: break
    print(f'w({a}, {b}, {c}) = {func(a, b, c)}')
