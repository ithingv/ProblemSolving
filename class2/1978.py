# 실버 4 소수 찾기

def check(num):
    list_ = [elem for elem in range(1,num+1) if num%elem==0]
    return True if len(list_) == 2 else False

n = int(input())
nums = list(map(int, input().split(' ')))
print(len(list(filter(lambda x: check(x)==True, nums))))