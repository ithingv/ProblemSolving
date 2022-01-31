from collections import deque

# dfs
def dfs(start):

    visited[start] = True
    print(f"{start} ", end="")

    for adj in path[start]:
        if not visited[adj]:
            dfs(adj)    

# bfs
def bfs(start):
    
    queue = deque()
    visited[start] = True
    queue.append(start)

    while queue:

        curr = queue.popleft()
        print(f"{curr} ", end="")

        for adj in path[curr]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

n, m, start = map(int, input().split())

path = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    path[v1].append(v2)
    path[v2].append(v1)

path = [sorted(lst) for lst in path]

dfs(start)
print()
visited = [False for _ in range(n + 1)]

bfs(start)