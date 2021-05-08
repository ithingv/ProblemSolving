#Bronze 3 ACM 호텔 ESSENTIAL	
T = int(input())
i = 0
while i < T:
    
    H, W, N = map(int, input().split())
    
    h = 1
    w = 1
    res = ""
    while True:
        
        if N < 1:
            print(res)
            break
            
        while h <= H and N > 0:
            
            if w <= W and w < 10:
                res = str(h) + "0" + str(w)
            elif w <= W and w >= 10:
                res = str(h) + str(w)
            h += 1
            N -= 1
        
        h = 1
        w += 1
    i += 1