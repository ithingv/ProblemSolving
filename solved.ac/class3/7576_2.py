import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))
    
    while queue:
        
        x, y = queue.popleft()
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
bfs()

if True in map(lambda x: 0 in x, graph):
    print(-1)
else:
    print(max(map(max, graph))-1)