# NOT solved
def solution(n, times):
    times = sorted(times)
    waiting = [[0, time] for time in times]
    pos = 0

    for k in range(n):
        upper = waiting[-1][0] + waiting[-1][1]
        for i in range(len(times)):
            if waiting[i][0] + waiting[i][1] <= upper:
                waiting[i][0] += waiting[i][1]
                break

        waiting = sorted(waiting, key=lambda x: x[0] + x[1])

    return waiting[-1][0]


print(solution(6, [7, 10]))