# 실버 4 통계학#Silver IV 2108	통계학	
from collections import Counter
import sys

N = int(input())
i = 0
arr = []
while i < N:
    arr.append(int(sys.stdin.readline()))
    i += 1
    
# 산술평균
print(round(sum(arr) / len(arr)))

# 중앙값
arr.sort()
left, right = 0, len(arr) - 1
print(arr[(left + right) // 2])

# 최빈값
counter = Counter(arr)
mode = counter.most_common()

if len(arr) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
        
# 범위
print(max(arr) - min(arr))