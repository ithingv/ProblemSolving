# 실버 3 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())
line_list = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(line_list)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for line in line_list:
        lines += line // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)