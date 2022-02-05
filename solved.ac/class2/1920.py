# 실버 4 수찾기

n = int(input())

while True:

    arr1 = list(map(int, input().split(' ')))
    if len(arr1) == n:
        break

    print("n개의 숫자를 입력해주세요")

m = int(input())

while True:
    
    arr2 = list(map(int, input().split(' ')))
    if len(arr2) == m:
        break

    print("m개의 숫자를 입력해주세요")

dict1 = dict()

for i in arr1:

    dict1[i] = 1

for i in arr2:
    
    if i in dict1:
        print(1)
    else:
        print(0)
