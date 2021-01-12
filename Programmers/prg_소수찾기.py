# Problem from Programmers
# Category: 완전탐색
# 소수찾기

import itertools

def isPrime(n):
    len_n = len(n)
    n = int(''.join(n))
    if n <= 1:
        return False
    elif len_n > len(str(n)):
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for d in range(3, int(n**0.5)+1):
            if n % d == 0:
                return False
        return True


def solution(numbers):
    answer = 0

    for r in range(1, len(numbers)+1):
        comb = set(list(itertools.permutations(numbers, r)))
        res = list(map(isPrime, comb))
        answer += sum(res)
    return answer


cases = ['17', '011']

for case in cases:
    print(solution(case))
    print('-'*20)
    # break