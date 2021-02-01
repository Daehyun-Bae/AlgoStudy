# Baekjoon no.6373 Round and Round We Go
# Keyword: Implementation
import sys

def chk_cyclic(num):
    if int(num) * (len(num) + 1) == int('9' * len(num)):
        return True
    else:
        return False

for number in sys.stdin:
    number = number.rstrip()
    if chk_cyclic(number):
        print(f'{number} is cyclic')
    else:
        print(f'{number} is not cyclic')