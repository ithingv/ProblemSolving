from collections import deque

# 상, 하, 좌, 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 

def bfs(x, y):
    q.append([x, y])
    check[x][y] = 1
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if s[nx][ny] == s[x][y] and check[nx][ny] == 0:
                    q.append([nx, ny])
                    check[nx][ny] = 1

N = int(input())
s = [list(input()) for _ in range(N)]
check = [[0] * N for _ in range(N)]
q = deque()

cnt = 0
for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end = ' ')

for i in range(N):
    for j in range(N):
        if s[i][j] == 'G':
            s[i][j] = 'R'

check = [[0] * N for _ in range(N)] 

cnt = 0
for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
          
