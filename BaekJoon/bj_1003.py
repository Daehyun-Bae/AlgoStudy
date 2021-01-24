# Baekjoon no.1003 피보나치 함수
# Keyword: Dynamic Programming

T = int(input())
for t in range(T):
    n = int(input())
    cnt = [[1, 0], [0, 1]]
    if n == 0 or n == 1:
        print(f'{cnt[n][0]} {cnt[n][1]}')
    else:
        while n > 1:
            cnt.append([cnt[0][0] + cnt[1][0], cnt[0][1] + cnt[1][1]])
            del cnt[0]
            n -= 1
        print(f'{cnt[1][0]} {cnt[1][1]}')
