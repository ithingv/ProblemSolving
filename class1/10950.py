n = int(input())
_list=[]
for i in range(n):
    _list.append(sum(list(map(int,input().split()))))
for elem in _list:
    print(elem)