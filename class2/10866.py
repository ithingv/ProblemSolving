#Silver IV 10866	덱 ESSENTIAL	

import sys
from collections import deque

N = int(input())
deque = deque()
i = 0 

while i < N:
              
    command = list(map(str, sys.stdin.readline().split()))

    if len(command) > 1 :

        if command[0] == 'push_front':
            num = command[-1]
            deque.appendleft(num)
        if command[0] == 'push_back':
            num = command[-1]
            deque.append(num)
    else:
        if command[0] == 'pop_front':
            try:
                print(deque.popleft())
            except IndexError:
                print(-1)
        if command[0] == 'pop_back':
            try:
                print(deque.pop())
            except IndexError:
                print(-1)
        if command[0] == 'size':
            print(len(deque))
        if command[0] == 'empty':
            print(1) if len(deque) == 0 else print(0)
        if command[0] == 'front':
            try:
                print(deque[0])
            except IndexError:
                print(-1)
        if command[0] == 'back':
            try:
                print(deque[-1])
            except IndexError:
                print(-1)

    i += 1