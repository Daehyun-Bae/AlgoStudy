# Baekjoon no.3830 교수님은 기다리지 않는다.

END = '0 0'
while True:
    test = input()
    if test == END:
        break
    n_sample, n_case = map(int, test.split())
    data = {}
    for c in range(n_case):
        command = input().split()
        if command[0] == '!':
            a, b, w = command[1:]
            if a not in data and b not in data :
                data[a] = [(b, -w)]
                data[b] = [(a, w)]
            if b in data:
                data[b].append((a, w))
            if a in data:
                data[a].append((b, -w))
        if command[0] == '?':
            a, b = command[1:]
            if a not in data or b not in data :
                print('UNKNOWN')
            
            
    print(n_sample, n_case)
