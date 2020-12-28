# Problem from Programmers
# Category: Hash
# 완주하지 못한 선수

'''
example-1
input:
    participant: [leo, kiki, eden]
    completion: [eden, kiki]
return: "leo"

example-2
input:
    participant: [marina, josipa, nikola, vinko, filipa]
    completion: [josipa, filipa, marina, nikola]
return: "vinko"

example-3
input:
    participant: [mislav, stanko, mislav, ana]
    completion: [stanko, ana, mislav]
return: "mislav"
'''

def solution(participant, completion):
    result = {}
    for p in participant:
        if p not in result:
            result[p] = 1
        else:
            result[p] += 1
    for c in completion:
        result[c] -= 1
    for k in participant:
        if result[k] != 0:
            answer = k
            break

    return answer