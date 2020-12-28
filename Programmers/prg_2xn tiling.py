# Problem from Programmers
# Category: practice
# 2xN tiling

def solution(n):
    a = 1
    b = 2
    if n <= 2:
        return [a, b][n-1]
    answer = a + b
    while n > 2:
        answer = a + b
        a = b
        b = answer
        n -= 1
    answer %= 1000000007
    return answer