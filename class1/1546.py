N = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
arr = [num / max_num * 100 for num in arr]
print(sum(arr) / len(arr))