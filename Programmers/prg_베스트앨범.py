# Problem from Programmers
# Category: Hash
# 베스트 앨범

from functools import reduce


def group_by_genres(acc, cur):
    idx, (genre, count) = cur
    if genre not in acc:
        acc[genre] = []
    acc[genre].append((idx, count))
    return acc


def solution(genres, plays):
    # Group by genre
    data_dict = reduce(group_by_genres, enumerate(zip(genres, plays)), {})

    # Count by genre
    genre_count = {k: reduce(lambda acc, cur: acc + cur[1], list(data_dict[k]), 0) for k in data_dict.keys()}

    # Compute genre priority
    prior_genre = [g[0] for g in sorted(genre_count.items(), key=lambda x: x[1], reverse=True)]

    answer = []
    for genre in prior_genre:
        if len(data_dict[genre]) == 1:
            answer.append(data_dict[genre][0][0])
        else:
            indices = [i[0] for i in sorted(data_dict[genre], key=lambda x: x[1], reverse=True)]
            answer += indices[:2]
    return answer


cases = [[["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]], # [4, 1, 3, 0]
         [["A", "A", "A", "B", "B", "C", "C", "C", "D"],	[10, 20, 20, 30, 40, 25, 30, 35, 85]],
         ]

for case in cases:
    print(solution(case[0], case[1]))
    print('-'*30)
