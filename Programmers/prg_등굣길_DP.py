# Problem from Programmers
# Category: Dynamic programming
# 등굣길


def solution(m, n, puddles):
    mem = [[-1 for i in range(m)] for j in range(n)]
    mem[0][0] = 1

    for k in range(1, m + n - 2):
        for i in range(k + 1):
            j = k - i
            if [i, j] in puddles:
                mem[i][j] = 0
            else:
                from_up = mem[i-1][j] if i - 1 >= 0 else 0
                from_left = mem[i][j - 1] if j - 1 >= 0 else 0
                try:
                    mem[i][j] = from_up + from_left
                except IndexError:
                    print(i, j)
                    exit()

    answer = 0
    return answer


cases = [(4, 3, [[2, 2]])]

for m, n, puddles in cases:
    print(solution(m, n, puddles))
    print('-'*20)

