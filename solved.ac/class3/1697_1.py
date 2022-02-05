from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    queue = deque()
    queue.append((n, 0))

    while queue:
        pos, dist = queue.popleft()
        
        if pos == k:
            return dist

        visited[pos] = 1

        # 이동할 수 있는 경우의 수
        if pos - 1 >= 0 and visited[pos-1] == 0:           
            # visited[pos - 1] = 1
            queue.append((pos - 1, dist + 1))

        if pos + 1 < len(visited) and visited[pos + 1] == 0:
            # visited[pos + 1] = 1
            queue.append((pos + 1, dist + 1))
        
        if pos * 2 < len(visited) and visited[pos * 2] == 0:
            # visited[pos * 2] = 1
            queue.append((2 * pos, dist + 1))

print(bfs())