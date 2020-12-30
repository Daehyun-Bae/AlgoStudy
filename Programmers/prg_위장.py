# Problem from Programmers
# Category: Hash
# 위장

import collections
def solution(clothes):
    count = dict(collections.Counter([c[1] for c in clothes]))
    answer = 1
    for v in list(count.values()):
        answer *= (v+1)
    return answer - 1


cases = [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
         [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]]

for case in cases:
    print(solution(case))