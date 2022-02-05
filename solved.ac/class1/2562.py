i = 0
arr = []
while i < 9:
    arr.append(int(input()))
    i += 1
print(max(arr))
print(arr.index(max(arr)) + 1)