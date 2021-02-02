# Baekjoon no.10942 팰린드롬?
# Keyword: String
import sys

pal = set()
not_pal = set()


def chk_palindrome(string, base_len):
    # print(string)
    for i in range(len(string) // 2):
        memo = (base_len + 1 + i, base_len + len(string) - i)
        if memo in pal:
            pal.add((base_len + 1, base_len + len(string)))
            print(f'{memo} already computed! - True')
            return True
        elif memo in not_pal:
            not_pal.add((base_len + 1, base_len + len(string)))
            print(f'{memo} already computed! - False')
            return False
        if string[i] != string[-(i + 1)]:
            not_pal.add((base_len + 1 + i, base_len + len(string) - i))
            return False

    pal.add((base_len + 1, base_len + len(string)))
    return True


N = int(sys.stdin.readline())
seq = list(sys.stdin.readline().rstrip('\n').split(' '))
print(seq)
T = int(sys.stdin.readline())
cnt = 0
for _ in range(T):
    s, e = map(int, sys.stdin.readline().split(' '))
    if chk_palindrome(''.join(seq[s - 1:e]), len(''.join(seq[:s - 1]))):
        print(1)
    else:
        print(0)
