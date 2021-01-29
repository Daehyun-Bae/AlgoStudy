# Baekjoon no.15649 N과 M(2)
# Keyword: Back tracking


n, m = map(int, input().split())


def dfs(arr,  depth):
    if depth == m:
        print(' '.join(map(str, result)))

    else:
        for i in range(len(arr)):
            if not arr[i] and result[depth - 1] < i + 1:
                result[depth] = i + 1
                depth += 1
                arr[i] = 1
                dfs(arr, depth)
                arr[i] = 0
                depth -= 1
                result[depth] = 0


for i in range(n):
    array = [0] * n
    result = [k + 1 for k in range(m)]

    array[i] = 1
    result[0] = i + 1
    dfs(array, 1)