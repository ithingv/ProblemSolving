import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ans = -1
    for i in range(x, M * N + 1, M):
        if i % N == y:
            ans = i + 1
            break
    print(ans)
