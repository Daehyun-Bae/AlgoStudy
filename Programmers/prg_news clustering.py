# Problem from Programmers
# Category: 2018 kakao blind recruitment
# News clustering

from collections import Counter


def solution(str1, str2):
    token1 = list(map(lambda x: str1[x:x + 2].lower(), range(len(str1) - 1)))
    token1 = Counter(list(filter(lambda x: x.isalpha(), token1)))

    token2 = list(map(lambda x: str2[x:x + 2].lower(), range(len(str2) - 1)))
    token2 = Counter(list(filter(lambda x: x.isalpha(), token2)))

    inter = token1 & token2
    inter = len(list(inter.elements()))

    union = token1 | token2
    union = len(list(union.elements()))

    if union == 0:
        return 65536
    answer = int((inter / union) * 65536)
    return answer