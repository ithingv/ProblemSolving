# 브론즈 2 부녀회장이 될테야

def get_num_people(k, n):
    
    arr = [[0] * n for _ in range(k + 1)]

    for i in range(n):
        arr[0][i] = i + 1

    for i in range(k + 1):
        arr[i][0] = 1

    i = 1

    while i <= k:
        j = 1
        while j < n:
            arr[i][j] = arr[i][j-1] + arr[i-1][j]
            j += 1
        i += 1
    print(arr[k][n-1])


T = int(input())
for i in range(T):
    
    k = int(input())
    n = int(input())
    
    get_num_people(k,n)