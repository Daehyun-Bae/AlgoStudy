# Problem from Programmers
# Category: Hash
# 전화번호 목록

def solution(numbers):
    if sum(numbers) == 0:
        answer = '0'
    else:
        numbers = map(str, sorted(numbers, key=lambda x: str(x)*3, reverse=True))   # condition: 0<= x <= 1000

        answer = ''.join(numbers)
    return answer


cases = [[6, 10, 2],
         [3, 30, 34, 5, 9],
         [1, 10, 0, 100],   # 1101000
         [0, 0, 0]]         # 0

for case in cases:
    print(solution(case))