# Problem from Programmers
# Category: Monthly code challenge S1
# 두 개 뽑아서 더하기

def solution(numbers):
    sum_num = []
    for k, i in enumerate(numbers):
        for j in numbers[k+1:]:
            sum_num.append(i + j)
    sum_num = set(sum_num)
    answer = sorted(sum_num)
    return answer