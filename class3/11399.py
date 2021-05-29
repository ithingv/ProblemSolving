from itertools import accumulate

N = int(input())
num = list(map(int, input().split()))

num.sort()
num = accumulate(list(num))
print(sum(num))
