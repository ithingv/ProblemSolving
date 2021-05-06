#Silver IV 4949	균형잡힌 세상	

while True:
    
    sentence = str(input())
    
    if sentence == '.':
        break
    
    i = 0
    stack = []
    balanced = True
    
    while i < len(sentence):
    
        curr_char = sentence[i]
        
        if curr_char == '(' or curr_char == '[': 
            stack.append(curr_char)
        if curr_char == ')' or curr_char == ']':
            
            if len(stack) == 0:
                balanced = False
                break
            else:    
                if curr_char == ')':
                    if stack[-1] != '(':
                        balanced = False
                        break
                    else:
                        stack.pop()
                if curr_char == ']':
                    if stack[-1] != '[':
                        balanced = False
                        break
                    else:
                        stack.pop()
        i += 1
        
    if balanced and len(stack) == 0:
        print("yes")
    else:
        print("no")