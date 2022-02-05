# 브론즈 1 설탕 배달

def sugar_delivery(N):
    res = []
    Y = 0
    
    while (N - 5*Y) > 0:
        
        if (N - 5*Y) % 5 == 0:
            res.append((N - 5*Y) // 5)
            break
            
        if (N - 5*Y) % 3 == 0:
            X = (N - 5 * Y) // 3
            res.append(X + Y)
        
        Y += 1

    return res

N = int(input())

if len(sugar_delivery(N)) == 0:
    print(-1)
else:
    print(min(sugar_delivery(N)))