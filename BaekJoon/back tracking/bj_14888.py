# Baekjoon no.14888 연산자 끼워넣기
# Keyword: Back tracking
import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ops = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def calc(pos):
