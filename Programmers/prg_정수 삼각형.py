# Problem from Programmers
# Category: Dynamic programming
# 정수 삼각형


def solution(triangle):
    memory = []
    memory.append([triangle[0][0]])
    for i in range(1, len(triangle)):
        memory_i = []
        row_i = triangle[i]
        for j in range(len(row_i)):
            v_ij = max(memory[max(i - 1, 0)][max(j - 1, 0)], memory[max(i - 1, 0)][min(j, len(row_i)-2)])
            v = v_ij + row_i[j]
            memory_i.append(v)
        memory.append(memory_i)

    answer = max(memory[-1])
    return answer


cases = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]]

for case in cases:
    print(solution(case))