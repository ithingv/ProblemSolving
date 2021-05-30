import sys

N = int(input())
i = 0
while i < N:
    
    n = int(input())
    wear = {}
    res = 1
    j = 0
    
    while j < n:
        name, category = map(str, sys.stdin.readline().split())
        if category not in wear:
            wear[category] = [name]
        else:
            wear[category].append(name)
        j += 1
    
    for category in wear.keys():
        res *= (len(wear[category]) + 1)
    
    print(res - 1)
    del(wear)    
    i += 1