# 실버 4 카드2

from collections import deque

N = int(input())

deque = deque([i for i in range(1, N+1)])
flag = True

while True:

    if len(deque) == 1:
        print(deque[0])
        break
        
    if flag == True:
        deque.popleft()
        flag = False
    else:
        deque.append(deque.popleft())
        flag = True