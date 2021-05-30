import sys
from itertools import accumulate

N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))
num = list(accumulate(num))
num.append(0)

i = 0
while i < M:
    start, end = map(int, sys.stdin.readline().split())
    print(num[end - 1] - num[start - 2])
    i += 1