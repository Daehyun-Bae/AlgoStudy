n, w, h = map(int, input().split(' '))
item = []
for _ in range(n):
    item.append(int(input()))

cri = (w**2 + h**2)**0.5
for i in item:
    print('DA' if i <=cri else 'NE')