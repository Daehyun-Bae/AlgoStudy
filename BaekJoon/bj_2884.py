# Baekjoon no.2884 알람 시계

h, m = map(int, input().split(' '))
h = (h + (m//45 - 1)) % 24
m = m - 45 - 60*(m//45 - 1)
print('{} {}'.format(h, m))
