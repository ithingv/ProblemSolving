#Silver 4 괄호 ESSENTIAL	

N = int(input())
i = 0

while i < N:
    
    j = 0
    sentence = str(input())    
    stack = []
    valid = True
    
    while j < len(sentence):
        curr_char = sentence[j]
        
        if curr_char == '(': 
            stack.append(curr_char)
        if curr_char == ')':
        
            if len(stack) == 0:
                valid = False
                break
            else:    
                if stack[-1] != '(':
                    valid = False
                    break
                else:
                    stack.pop()
        j += 1
    if valid and len(stack) == 0:
        print("YES")
    else:
        print("NO")    
    i += 1
