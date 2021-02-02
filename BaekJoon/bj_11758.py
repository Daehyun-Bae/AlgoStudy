# Baekjoon no.11758
# Keyword: Geometric

p1 = list(map(int, input().split(' ')))
p2 = list(map(int, input().split(' ')))
p3 = list(map(int, input().split(' ')))

# 삼각형 넓이 공식 풀이
# s = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
# if s == 0:
#     print(0)
# else:
#     print(1 if s > 0 else -1)

# 기울기  풀이
if p2[0] != p1[0]:
    r = (p2[1] - p1[1]) / (p2[0] - p1[0])
    # ans = r * p3[0] + (p1[1] - p1[0] * r)
    if p3[1] > round(r * p3[0] + (p1[1] - p1[0] * r), 1):
        print(1 if p1[0] < p2[0] else -1)
    elif p3[1] < round(r * p3[0] + (p1[1] - p1[0] * r), 1):
        print(-1 if p1[0] < p2[0] else 1)
    else:
        print(0)
else:
    if p3[0] == p1[0]:
        print(0)
    elif p3[0] < p1[0]:
        print(1 if p1[1] < p2[1] else -1)
    else:
        print(-1 if p1[1] < p2[1] else 1)