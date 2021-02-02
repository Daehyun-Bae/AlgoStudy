# Baekjoon no.2577 숫자의 개수
# Keyword: String
from collections import Counter
a, b, c = int(input()), int(input()), int(input())
n = a*b*c
count = {i: 0 for i in range(10)}
count.update(dict(Counter(int(i) for i in str(n))))
for v in count.values():
    print(v)