# Baekjoon no.9665 돌게임

n = int(input())
win = 'CY' if ((n // 3) % 2 == 0) == ((n % 3) % 2 == 0) else 'SK'
print(win)
