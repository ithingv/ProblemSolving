import sys

num = int(sys.stdin.readline())
T = [ 1 for i in range(num)]
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(T)):
    T[i] = 1
    for j in range(i,-1,-1):
        if arr[j]<arr[i] and T[j]>=T[i]:
            T[i] = T[j]+1

sys.stdout.write(str(max(T)))

