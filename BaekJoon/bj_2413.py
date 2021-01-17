# Baekjoon no.2413 비슷한 순열
# Category: Greedy

n = int(input())
arr = list(map(int, input().split(' ')))


def solution(n, arr):
    # store whether each elements is swapable and its index
    memo = {el: [True, i] for i, el in enumerate(arr)}

    # Copy given array
    answer = [c for c in arr]

    for k in arr:
        # if the number is 1 and swapable, switch off
        if k == 1 and memo[1][0]:
            memo[1][0] = False

        else:
            # Swap if possible
            if memo[k][0] and memo[k-1][0]:
                memo[k][0] = False
                memo[k-1][0] = False
                answer[memo[k][1]] = k - 1
                answer[memo[k-1][1]] = k
            # Else, switch off
            else:
                memo[k][0] = False

    return ' '.join(map(str, answer))


print(solution(n, arr))