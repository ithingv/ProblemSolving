N, M, V = map(int, input().split())
matrix = [[0]* (N+1) for _ in range(N+1)]

for _ in range(M):
    edge = list(map(int, input().split()))
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1

def dfs(current_node, row, visited):
    visited += [current_node]
    for search_node in range(len(matrix[current_node])):
        if row[current_node][search_node] and search_node not in visited:
            visited = dfs(search_node, row, visited)
    return visited

def bfs(start):
    queue = [start]
    visited = [start]

    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
             #현재 노드와 연결된 모든 간선에 대해
             if matrix[current_node][search_node] and search_node not in visited:
                 queue += [search_node]
                 visited += [search_node]
    return visited

print(*dfs(V, matrix, []))
print(*bfs(V))