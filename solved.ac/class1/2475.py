arr = map(int, input().split())
ac = 0
for num in arr:
    ac += (num * num)
print(ac % 10)