# 2020 KAKAO BLIND RECRUITMENT: 자물쇠와 열쇠

def rotate(pt, m):
    result = []
    for r, c in pt:
        x = c
        y = (m-1) - r
        result.append((x, y))
    return result


def chk_key(key, lock, i, j, n):
    n_pass = 0
    for r, c in key:
        if (0 <= r + i < n) and (0 <= c + j < n):
            if lock[r + i][c + j] == 1:
                break
            else:
                n_pass += 1
    return n_pass


def solution(key, lock):
    n = len(lock[0])
    m = len(key[0])
    ones = []
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                ones.append((i, j))
    zeros = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                zeros.append((i, j))

    if len(zeros) > len(ones):
        return False

    key_90 = rotate(ones, m)
    key_180 = rotate(key_90, m)
    key_270 = rotate(key_180, m)
    for i in range(1-n, n):
        for j in range(1-n, n):
            n_pass = chk_key(ones, lock, i, j, n)
            if n_pass == len(zeros):
                return True

            n_pass = chk_key(key_90, lock, i, j, n)
            if n_pass == len(zeros):
                return True

            n_pass = chk_key(key_180, lock, i, j, n)
            if n_pass == len(zeros):
                return True

            n_pass = chk_key(key_270, lock, i, j, n)
            if n_pass == len(zeros):
                return True
    return False


cases = [[[[0, 0, 0],
           [1, 0, 0],
           [0, 1, 1]],
          [[1, 1, 1],
           [1, 1, 0],
           [1, 0, 1]]],
         [[[0, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [1, 0, 0, 0]],
          [[0, 1, 1, 1],
           [1, 1, 1, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 1]]],
         ]

for key, lock in cases:
    print(solution(key, lock))
