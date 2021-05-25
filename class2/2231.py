#Bronze II 2231	분해합	

N = input()
M = len(N)
N = int(N)
temp = N - (9 * M)

while True:
    
    if temp == N:
        print(0)
        break
        
    j = 0
    res = 0
    while j < M:
        res += int(str(temp)[j])
        j += 1
        
    if res + temp == N:
        print(temp)
        break
        
    temp += 1