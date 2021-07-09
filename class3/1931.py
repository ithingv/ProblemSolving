n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# 가장 빨리 끝나는 회의 먼저 배정하고, 똑같은 시간에 끝나는 회의라면 먼저 시작하는 회의를 우선순위로 둔다.
arr = sorted(arr, key = lambda x: (x[1], x[0]))

count = 1
# 첫 번째 회의가 끝나는 시간
prev = arr[0][1]
for sch in arr[1:]:
    # 다음 회의의 시작시간이 이전 회의가 끝나는 시간보다 크거나 같다 = 회의를 열 수 있다
    if prev <= sch[0]:
        prev = sch[1]
        count += 1

print(count)
    
