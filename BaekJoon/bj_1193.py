# Baekjoon no.1193

def solution(n):
    k = 1
    while True:
        if n <= k*(k+1)/2:
            break
        k += 1
    total = k + 1
    order = int(n - k*(k-1)/2)
    if k % 2 == 0:
        return '{}/{}'.format(order, total - order)
    else:
        return '{}/{}'.format(total - order, order)

for i in range(1, 20):
    print(i, solution(i))