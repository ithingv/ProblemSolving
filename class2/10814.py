# 실버 5 나이순 정렬

num = int(input())
arr = []
for i in range(num):

    age, name = list(map(str, input().split(' ')))
    arr.append((int(age),name))

arr = sorted(arr, key = lambda x: x[0])

for info in arr:
    print(info[0], info[1])
