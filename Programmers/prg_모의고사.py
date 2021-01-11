# Problem from Programmers
# Category: 완전 탐색
# 모의고사

def solution(answers):
    student = {1: 0, 2: 0, 3: 0}
    table = [[1, 2, 3, 4, 5],
             [1, 3, 4, 5],
             [3, 1, 2, 4, 5]]

    for i, ans in enumerate(answers):
        if table[0][i % 5] == ans:
            student[1] += 1

        if (i % 2 == 0 and ans == 2) or (i % 2 == 1 and table[1][(i % 8) // 2] == ans):
            student[2] += 1

        if table[2][(i % 10) // 2] == ans:
            student[3] += 1

    best_score = max(student.values())

    answer = [k[0] for k in student.items() if k[1] == best_score]

    return answer


cases = [[1, 2, 3, 4, 5],
         [1, 3, 2, 4, 2]
         ]

for case in cases:
    print(solution(case))
    print('-' * 30)
