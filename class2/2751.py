import sys
N = int(sys.stdin.readline())

arr = []
i = 0
while i < N:
    arr.append(int(sys.stdin.readline()))
    i += 1

arr.sort()
for num in arr:
    print(num)