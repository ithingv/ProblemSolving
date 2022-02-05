# 2206 G4
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range(n)]
queue = deque()
queue.append((0, 0, 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()

    # 벽으로 가로막힌 경우
    if graph[x][y] == 1:
        continue
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not graph[nx][ny] and visited[x][y] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

print(graph)



# 벽을 부순다 ---> 1을 0으로 바꾼다.
