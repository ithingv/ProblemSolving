#Silver 4 10828	스택 ESSENTIAL	

import sys

N = int(input())
stack = []
i = 0 
while i < N:
              
    command = list(map(str, sys.stdin.readline().split()))

    if len(command) > 1 :
        num = command[-1]
        stack.append(num)
    else:
        if command[0] == 'pop':
            try:
                print(stack.pop())
            except IndexError:
                print(-1)
        if command[0] == 'size':
            print(len(stack))
        if command[0] == 'empty':
            print(1) if len(stack) == 0 else print(0)
        if command[0] == 'top':
            try:
                print(stack[-1])
            except IndexError:
                print(-1)
    i += 1