import sys

N = int(input())
i = 0
dp = [0] * 101
dp[0] = 0
dp[1],dp[2],dp[3] = 1,1,1
dp[4],dp[5] = 2,2

while i < N:
    
    n = int(sys.stdin.readline())
    if n < 6:
        print(dp[n])
    else:
        j = 6
        while j <= n:
            dp[j] = dp[j-1] + dp[j-5]
            j += 1
        print(dp[n])
    i += 1