'''
ex
citations	    return
[3, 0, 6, 1, 5] 3
'''

def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = len([i+1 for i in range(len(citations)) if i+1 <= citations[i]])

    # another answer
    # answer = list(map(min, enumerate(citations, start=1)))

    return answer

cases = [[3, 0, 6, 1, 5],   # 3
         [0, 0, 0, 0, 0],   # 0
         [25, 8, 5, 3, 3],  # 3
         [10, 8, 5, 4, 3]  # 4
         ]

for case in cases:
    print(solution(case))