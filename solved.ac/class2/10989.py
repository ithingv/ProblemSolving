# 실버 5 수 정렬하기 3

import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
            
