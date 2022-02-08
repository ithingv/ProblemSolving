# 연구소 G5
from collections import deque
import sys

# 1. 벽을 어디에 위치 시킬 것인지 (여유 3개)
     # 벽을 세울 수 있는 위치
     # 효과적으로 벽을 세워야한다. (완전 탐색)
# 2. 바이러스(2)가 점점 확산되는 문제
    # 벽이 없는 곳(0)인 곳은 바이러스가 확산될 수 있다.
# 3. 벽 3개를 위치 시키고 나서 안전지대의 개수를 반환하는 함수 
    # 전체 안전지대의 개수 = N * M - (바이러스의 개수 + 벽의 개수)

# 헷갈리는 점
# 바이러스를 기준으로 동서남북을 탐색하며 벽을 어디에 둘지 탐색을 하려하는데 
# 무작정 1을 놓을 수 있는 위치에서 벽을 설치하고 남아있는 카운트(wall_cnt)를 줄여도 되는 것인지
# 아래 이중 for문에서 dfs(i,j)에서 먼저 호출된 dfs가 남아있는 벽을 모두 사용하는 경우 
# 늦게 호출되는 dfs는 벽을 사용하지 못할 수 도 있으므로 반드시 효과적이라고 할 수 없을 것 같다.

# 단지번호 붙이기 문제
# 토마토 문제 복기

def dfs(x, y):
    global wall_cnt

    # 벽을 세울 수 있는 경우
    if graph[x][y] == 0:
        # 벽을 세운다
        graph[x][y] = 1
        visited[x][y] = 1
        wall_cnt -= 1

    if wall_cnt == 0:
        # 지금까지 방문했던 안전지대를 반환
        return sum(visited)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            dfs(nx, ny)

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
queue = deque()
visited = [[0 for i in range(M)] for j in range(N)]
wall_cnt = 3
safe_zone_cnt = 0

# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽의 개수
for i in range(N):
    for j in range(M):
        # 안전지대
        if graph[i][j] == 1:
            wall_cnt += 1

# 바이러스가 있는 곳 부터 깊이 우선 탐색
for i in range(N):
    for j in range(M):
        # 바이러스가 있는 위치
        if graph[i][j] == 2:
            dfs(i, j)