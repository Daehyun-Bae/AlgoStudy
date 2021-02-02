# Baekjoon no.10942 팰린드롬?
# Keyword: String, Dynamic Programming
import sys

pal = set()
not_pal = set()


def chk_palindrome(start, end):
    s = start
    e = end
    while s < e:
        memo = (s, e)
        if memo in pal:
            print(f'{memo} already computed! - True')
            return True
        elif memo in not_pal:
            print(f'{memo} already computed! - False')
            return False
        if seq[s-1] != seq[e-1]:
            not_pal.add(memo)
            return False
        s += 1
        e -= 1
    pal.add((start, end))
    return True


def chk_palindrome2(sequence, start, end):
    # Pre-computed check
    if (start, end) in pal:
        print(f'{(start, end)} already computed! - True')
        return True
    elif (start, end) in not_pal:
        print(f'{(start, end)} already computed! - False')
        return False
    s = start
    e = end
    left = ''
    right = ''
    while s < e:
        if (s, e) in pal:
            print(f'{(s, e)} already computed! - True')
            return True
        elif (s, e) in not_pal:
            print(f'{(s, e)} already computed! - False')
            return False

        left = left + sequence[s-1]
        right = sequence[e-1] + right
        while len(left) != len(right):
            if e < s:
                break
            if len(left) < len(right):
                s += 1
                left = left + sequence[s-1]
            else:
                e -= 1
                right = sequence[e-1] + right
        for i in range(len(left)):
            if left[i] != right[-(i + 1)]:
                not_pal.add((start, end))
                not_pal.add((s, e))
                return False
        s += 1
        e -= 1
    pal.add((start, end))
    return True


N = int(sys.stdin.readline())
seq = list(sys.stdin.readline().rstrip('\n').split(' '))
print(seq)
T = int(sys.stdin.readline())
cnt = 0
for _ in range(T):
    S, E = map(int, sys.stdin.readline().split(' '))
    if chk_palindrome(S, E):
    # if chk_palindrome2(seq, S, E):
        print(1)
    else:
        print(0)
