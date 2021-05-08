# 브론즈 2 Hashing

L = int(input())
word = input()
res = 0
cnt = 0

for alpha in word:
    res += (ord(alpha) - 96) * pow(31, cnt)
    if res > 2147483647:
        res %= 1234567891
    cnt += 1

print(res)