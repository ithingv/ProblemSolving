import sys
from collections import deque

input = sys.stdin.readline
   
def solve(n,m) :
    
    snake = [0 for _ in range(101)]
    ledder = [0 for k in range(101)]
    #합쳐서 관리하는게 더 나을 것 같다.
    
    visited = [False for _ in range(101)]

    for i in range(n) :
        x , y = map(int,input().split())
        ledder[x] = y
    
    for j in range(m) :
        x , y = map(int,input().split())
        snake[x] = y

    q = deque()

    q.append((1,0))
    visited[1] = True

    ans = float("inf")

    while q :
        
        front = q.popleft()

        if front[0] == 100 :
            ans = min(ans, front[1])
            continue


        for i in range(1,7) :
            new = front[0]+i
            
            if new > 100 :continue
            
            if visited[new] == True :
                continue
            
            visited[new] = True

            if snake[new] != 0 :
                new = snake[new]
            
            if ledder[new] != 0 :
                new = ledder[new]

            q.append((new,front[1]+1))
    
    print(ans)
        
        
if __name__ =="__main__" :
    n,m = map(int,input().split())
    solve(n,m)
