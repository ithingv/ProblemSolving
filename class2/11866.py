#Silver IV 11866	요세푸스 문제 0 ESSENTIAL	

N, K = map(int, input().split())

arr = [ i for i in range(1, N+1)]
x_cnt = 0
curr_pos = 0
print("<", end = "")

while True:
    
    if x_cnt == N:
        print(">")
        break
    
    cnt = 0 
    
    while True:
                
        if arr[curr_pos] == 'X':
            curr_pos += 1

        else:
            if cnt == K - 1:
                x_cnt += 1
                if x_cnt == N:
                    print(arr[curr_pos], end = "")
                else:
                    print(arr[curr_pos], end = ", ")
                arr[curr_pos] = 'X'
                break
            else:
                curr_pos += 1
                cnt += 1
                
        if curr_pos == N:
            curr_pos = 0