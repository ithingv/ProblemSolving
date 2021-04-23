from functools import reduce

try:
    n = int(input())
    N = str(input())
    if not 1<=len(N)<=100:
        exit()
    print(reduce(lambda x,y: int(x)+int(y), N))

except:
    exit()