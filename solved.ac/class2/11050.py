# 브론즈 1 이항 계수1

factorial_memo = {}

def factorial(n):
    if n < 2:
        return 1
    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n-1)
    return factorial_memo[n]

N, K = map(int, input().split())

print(factorial(N) // factorial(N-K) // factorial(K))
