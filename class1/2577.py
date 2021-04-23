i = 0
nums = 1
while i < 3:
    nums *= int(input())
    i += 1
nums = str(nums)
j = 0
while j < 10:
    cnt = 0
    k = 0
    while k < len(nums):
        if int(nums[k]) == j:
            cnt += 1
        k += 1
    print(cnt)
    j += 1