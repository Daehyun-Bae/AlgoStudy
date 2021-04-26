from collections import deque
a = [1, 3, 2, 4, 5]
b = deque(a)
print(b)
b = deque(sorted(b))
print(b.popleft())