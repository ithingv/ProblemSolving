# 브론즈 2 블랙잭

import sys

NM = list(map(int, input().split(' ')))
N = NM[0]
M = NM[1]
arr = list(map(int, input().split(' '))) 

ascending=True
maxSum=0

if len(arr) !=N:
    sys.exit()
else:
    for i in range(len(arr)-2):
        for j in range(1,len(arr)-1):
            if i>j or i==j:
                continue
            for k in range(2, len(arr)):

                if j>k or j==k:
                    continue
                if arr[i] + arr[j] + arr[k] <= M and arr[i] + arr[j] + arr[k] > maxSum:
                    maxSum = arr[i] + arr[j] + arr[k]
                else:
                    continue
print(maxSum)
