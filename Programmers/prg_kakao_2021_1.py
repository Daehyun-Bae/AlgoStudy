# KAKAO BLIND 합승 택시 요금
# Category: Floyd-Warshall


def solution(n, s, a, b, fares):
    # initialize
    grid = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                grid[i][j] = 0

    for src, dst, w in fares:
        grid[src][dst] = w
        grid[dst][src] = w

    # Floyd-Warshall algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

    answer = grid[s][a] + grid[s][b]
    for k in range(1, n + 1):
        answer = min(answer, grid[s][k] + grid[k][a] + grid[k][b])
    return answer


cases = [[6, 4, 6, 2,
          [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
         [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
         [6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]]]

for case in cases:
    n, s, a, b, fares = case
    print(solution(n, s, a, b, fares))
    print('-' * 80)
