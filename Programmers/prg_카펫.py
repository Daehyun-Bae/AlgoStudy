# Problem from Programmers
# Category: 완전탐색
# 카펫


def solution(brown, yellow):
    candidates = [(int(yellow/i), i) for i in range(1, (yellow+1)//2+1) if yellow % i == 0]
    candidates = list(filter(lambda x: x[0] >= x[1], candidates))
    print(candidates)
    for a, b in candidates:
        if a*2 + b*2 + 4 == brown:
            return [a+2, b+2]

    return -1

cases = [[10, 2], [8, 1], [24, 24]]

for b, y in cases:
    print(solution(b, y))
    print('-'*20)
    # break