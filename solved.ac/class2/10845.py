#Silver 4 10845	큐 ESSENTIAL	
import sys

N = int(input())
queue = []
i = 0 
while i < N:
              
    command = list(map(str, sys.stdin.readline().split()))

    if len(command) > 1 :
        num = command[-1]
        queue.append(num)
    else:
        if command[0] == 'pop':
            try:
                print(queue.pop(0))
            except IndexError:
                print(-1)
        if command[0] == 'size':
            print(len(queue))
        if command[0] == 'empty':
            print(1) if len(queue) == 0 else print(0)
        if command[0] == 'front':
            try:
                print(queue[0])
            except IndexError:
                print(-1)
        if command[0] == 'back':
            try:
                print(queue[-1])
            except IndexError:
                print(-1)

    i += 1