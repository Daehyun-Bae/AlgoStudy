import sys
n = int(sys.stdin.readline().rstrip('\n'))
case = 1
while n > 0:
    s = int(sys.stdin.readline().rstrip('\n'))
    if n > 1:
        for l in range(1, n-1):
            line = list(map(int, sys.stdin.readline().rstrip('\n').split()))
            s += line[0] + line[-1]
        s += sum(map(int, sys.stdin.readline().rstrip('\n').split()))
    print(f'Case #{case}:{s}')
    case += 1
    n = int(sys.stdin.readline().rstrip('\n'))