# Baekjoon no.2447 별찍기-10
# Keyword: Recursive, Divide and conquer

n = int(input())

def star(k):
    p = []
    if k == 3:
        p.append('***')
        p.append('* *')
        p.append('***')
        return p
    else:
        kk = k//3
        prev_pattern = star(kk)
        for i in range(kk):
            p.append(prev_pattern[i]*3)
        for i in range(kk):
            p.append(prev_pattern[i] + ' '*kk + prev_pattern[i])
        for i in range(kk):
            p.append(prev_pattern[i]*3)
        return p

result = star(n)
for l in result:
    print(l)