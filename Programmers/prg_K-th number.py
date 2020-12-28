# Problem from Programmers
# Category: Sorting
# K번째 수

'''
example
input:
    array: [1, 5, 2, 6, 3, 7, 4]
    commands: [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
return: [5, 6, 3]
'''

def solution(array, commands):
    answer = []
    for command in commands:
        l, r, k = command
        answer.append(sorted(array[l - 1:r])[k - 1])

    return answer