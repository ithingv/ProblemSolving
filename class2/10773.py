#Silver 4 제로	

K = int(input())
i = 0
stack = []
while i < K:
    
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
    i += 1
    
print(sum(stack))