# Baekjoon no.15649 N과 M(3)
# Keyword: Back tracking


n, m = map(int, input().split())


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))

    else:
        for i in range(n):
            result[depth] = i + 1
            dfs(depth + 1)


result = [0] * m
dfs(0)