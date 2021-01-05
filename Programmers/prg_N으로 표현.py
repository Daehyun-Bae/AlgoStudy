# Problem from Programmers
# Category: Dynamic programming
# N으로 표현


def branch(base, N):
    return [base+N, base-N, base*N, base//N]


def solution(N, number):
    table = {N: 1}

    if N == number:
        return 1

    for i in range(1, 8):
        number_N = list(filter(lambda x: table[x] == i, table.keys()))
        for c in number_N:
            branches = branch(base=c, N=N) + [int('1'*(i+1)) * N]
            if number in branches:
                return i + 1
            for b in branches:
                if b not in table:
                    table[b] = i + 1

    return -1


cases = [(5, 12),
         (2, 11)]

for n, number in cases:
    print(solution(n, number))