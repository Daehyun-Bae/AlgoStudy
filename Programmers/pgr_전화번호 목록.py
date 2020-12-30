# Problem from Programmers
# Category: Hash
# 전화번호 목록

from functools import reduce


def group_func(acc, cur):
    length = len(cur)
    if length not in acc:
        acc[length] = []
    acc[length].append(cur)
    return acc


def solution(phone_book):
    phone_len_dict = reduce(group_func, phone_book, {})

    for phone_number in phone_book:
        length = len(phone_number)
        tg = [k for k in phone_len_dict.keys() if int(k) > length]

        for k in tg:
            for number in phone_len_dict[k]:
                if number[:length] == phone_number:
                    return False
    answer = True
    return answer


cases = [["119", "97674223", "1195524421"], # false
         ["123","456","789"],               # true
         ["12","123","1235","567","88"]]    # false

for case in cases:
    print(solution(case))