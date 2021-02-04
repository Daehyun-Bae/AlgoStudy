def solution(n):
    answer = 1
    if n < 3:
        return 1
    k = 1
    while k * (k + 1) / 2 < n:
        if (n - int(k * (k + 1) / 2)) % (k + 1) == 0:
            base = (n - int(k * (k + 1) / 2))
            # for i in range(k):
            #     print(base // (k+1) + i+1, end= ' ')
            # print()
            print(f'k: {k}')
            answer += 1
        k += 1

    return answer

cases = [6, 15]
for case in cases:
    print(solution(case))
    print('-'*40)