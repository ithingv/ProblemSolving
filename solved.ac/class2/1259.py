# 브론즈 1 팰린드롬수

is_palindrome = True

while(True):
    
    num = input()
    if num == '0':
        break
    left = 0
    right = len(num) - 1
    is_palindrome = False
    while left <= right:
        if num[left] != num[right]:
            print('no')
            is_palindrome = False
            break
        left += 1
        right -= 1
        is_palindrome = True
    if is_palindrome:
        print('yes')    