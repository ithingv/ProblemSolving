n, r, c = map(int, input().split())
def find(r, c): # 사분면 찾는 함수
    if 0 <= r < 2 ** (n-1) and 0 <= c < 2 ** (n-1):
        return 1
    elif 0 <= r < 2 ** (n-1) and 2 ** (n-1) <= c < 2 ** (n):
        return 2
    elif 2 ** (n-1) <= r < 2 ** (n) and 0 <= c < 2 ** (n-1):
        return 3
    else:
        return 4
 
def reallocate(): # 사분면을 쪼갠후 좌표값을 재배치
    global r, c, n
 
    if res == 2: # 2사분면인 경우
        c -= 2 ** (n-1)
    elif res == 3: # 3사분면인 경우
        r -= 2 ** (n-1)
    elif res == 4: # 4사분면인 경우
        r -= 2 ** (n-1)
        c -= 2 ** (n-1)
    n -= 1
 
ans = 0
while True:
    if n <= 0:
        break
    res = find(r, c)
    ans = ans + (res-1) * (4 ** (n-1))
    reallocate()
 
print(ans)
