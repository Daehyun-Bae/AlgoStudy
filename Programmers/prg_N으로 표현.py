# Problem from Programmers
# Category: Dynamic programming
# N으로 표현
from itertools import product

def calc(base, N):
    return list(filter(lambda x: x!=0, [base+N, base-N, base*N, base//N]))


def solution(N, number):
    table = {N: 1}

    if N == number:
        return 1

    for i in range(2, 9):

        if str(N)*i == str(number): return i
        table[int(str(N)*i)] = i

        for j in range(1, i):
            arr1 = list(filter(lambda x: table[x] == j, table.keys()))
            arr2 = list(filter(lambda x: table[x] == i-j, table.keys()))
            for b, n in product(arr1, arr2):
                result = calc(b, n)
                if number in result: return i
                for r in result:
                    if r not in table:
                        table[r] = i
    
    return -1
    '''
    table = {N: 1}

    if N == number:
        return 1

    for i in range(1, 8):
        number_N = list(filter(lambda x: table[x] == i, table.keys()))
        for c in number_N:
            branches = branch(base=c, N=N) + [int('1'*(i+1)) * N]
            if number in branches:
                print(table)
                return i + 1
            for b in branches:
                if b not in table:
                    table[b] = i + 1
    '''
    return -1


cases = [(5, 12),
         (2, 11),
         (7, 76),
         (3, 333)]

for n, number in cases:
    print(solution(n, number))
    print('-'*20)
    # break