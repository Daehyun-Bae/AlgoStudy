# Baekjoon no.11729 하노이 탑
# Keyword: Recursive
n = int(input())

def h(n, s, d):
    if n == 1:
        return [[s, d]]
    else:
        return h(n-1, s, 6-(s+d)) + [[s, d]] + h(n-1, 6-(s+d), d)

result = h(n, 1, 3)
print(len(result))
for move in result:
    print(' '.join(map(str,move)))