N = int(input())
P = int(input())
graph = [[0]*(N+1) for _ in range(N+1)] 
arr= []

for _ in range(P): 
    x, y = map(int, input().split()) 
    graph[x][y], graph[y][x] = 1, 1 

def dfs(v): 
    arr.append(v) 
    for k in range(1, N+1):
        if k not in arr and graph[v][k] == 1:
            dfs(k) 
    return (len(arr) - 1)
 
print(dfs(1))
