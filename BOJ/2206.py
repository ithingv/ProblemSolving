from collections import deque
import sys

def bfs(graph, n, m):

    # 동서남북으로 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1
    
    while queue:
        x, y, w = queue.popleft()
        
        # 마지막 노드에 도착했을 때
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs(graph, n, m))