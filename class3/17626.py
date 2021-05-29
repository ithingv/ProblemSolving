import math

def is_square(n):
    return int(n ** 0.5) ** 2 == n 

n = int(input())
dp = [0] * (n+1)
dp[0], dp[1] = 0, 1

i = 2
while i <= n: 
    if is_square(i):
        dp[i] = 1
    else:
        dp[i] = i
    i += 1
    
i = 2
while i <= n:
    j = 1
    while j <= int(math.sqrt(i)):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
        j += 1
    i += 1

print(dp[n])
