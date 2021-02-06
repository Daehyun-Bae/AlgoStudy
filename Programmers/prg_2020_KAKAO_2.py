# 2020 KAKAO BLIND RECRUITMENT: 외벽 점검


def solution(n, weak, dist):
    segments = [(weak[(i+1) % len(weak)] - weak[i]) % n for i in range(len(weak))]
    segments = sorted(segments, reverse=True)
    dist = sorted(dist, reverse=True)

    for k in range(1, len(dist)):
        if sum(segments[k:]) > sum(dist):
            print(f'{sum(segments[1:])} > {sum(dist)}')
            continue
        # total_len = sum(segments[k:])
        # if total_len <= sum(dist[:k]):
        #     return k
        sucess = True
        bound = sum(dist[:k])
        for s in segments[k:]:
            bound -= s
            print(bound)
            if bound < 0:
                sucess = False

        if sucess:
            print('answer ', k)
            return k
    return -1


cases = [[12, [1, 5, 6, 10], [1, 2, 3, 4]],
         [12, [1, 3, 4, 9, 10], [3, 5, 7]],
         [31, [0, 2, 8, 11, 19, 24], [6, 2, 3]]]
for n, weak, dist in cases:
    print(solution(n, weak, dist))