# Baekjoon no.15649 N과 M(1)
# Keyword: Back tracking


n, m = map(int, input().split())
result = [0] * m


def dfs(arr,  depth):
    if depth == m:
        print(' '.join(map(str, result)))

    else:
        for i in range(len(arr)):
            if not arr[i]:
                result[depth] = i + 1
                depth += 1
                arr[i] = 1
                dfs(arr, depth)
                arr[i] = 0
                depth -= 1


array = [0] * n
dfs(array, 0)