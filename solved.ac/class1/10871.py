N, X = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
while i < N:
    if arr[i] < X:
        print(arr[i], end= " ")
    i += 1