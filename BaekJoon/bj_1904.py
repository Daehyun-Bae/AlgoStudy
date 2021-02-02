# Baekjoon no.1904 01타일
# Keyword: Dynamic programming
n = int(input())

a, b = 1, 2


def solution(n):
    global a , b
    if n <= 2:
        return [a, b][n - 1]
    answer = a + b
    while n > 2:
        answer = (a + b) % 15746
        a = b
        b = answer
        n -= 1
    return answer


print(solution(n))
