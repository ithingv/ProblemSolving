import sys

num = int(sys.stdin.readline())
arr = [0 for _ in range(num+1)]

arr[1] = 1

if num>1:
    arr[2] = 3

for i in range(3,num+1):
    arr[i] = arr[i-1] + 2*arr[i-2]

sys.stdout.write(str(arr[num]%10007))