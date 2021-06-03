N = int(input())
cost_per_home = []

# 각 집마다 색깔 별 가격을 저장한다. 
for _ in range(N):
    cost_per_home.append(list(map(int, input().split())))
    
    dp = [cost_per_home[0]]

for i in range(1, N):
    cost_per_color = []
    
    temp_red = min(dp[i - 1][1], dp[i - 1][2])
    cost_per_color.append(temp_red + cost_per_home[i][0])

    temp_green = min(dp[i - 1][0], dp[i - 1][2])
    cost_per_color.append(temp_green + cost_per_home[i][1])

    temp_blue = min(dp[i - 1][0], dp[i - 1][1])
    cost_per_color.append(temp_blue + cost_per_home[i][2])
    
    dp.append(cost_per_color)
    
print(min(dp[N - 1]))
