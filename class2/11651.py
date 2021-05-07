#Silver V 11651	좌표 정렬하기 2	

N = int(input())
arr = []

for i in range(N):
    x,y = list(map(int, input().split(' ')))
    arr.append((x,y))

arr = sorted(arr, key= lambda x : (x[1], x[0]))

for elem in arr:
    print(elem[0], elem[1])