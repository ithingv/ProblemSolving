# 실버 5 좌표 정렬하기 1

N = int(input())
arr = []

for i in range(N):
    x,y = list(map(int, input().split(' ')))
    arr.append((x,y))

arr = sorted(arr)

for elem in arr:
    print(elem[0], elem[1])