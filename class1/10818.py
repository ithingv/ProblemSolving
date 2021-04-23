try:
    n = int(input())
    _list = list(map(int,input().split()))
    if len(_list)==n and 1<=n<=1000000:
        print("{} {}".format(min(_list), max(_list)))
except:
    exit()