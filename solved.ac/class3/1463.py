import sys

num = int(input())
arr = [ 0  for _ in range(num+1)]

for i in range(1, num+1):
    if i==1:
        continue
    val= []
    if i%3==0:
        val.append(arr[i//3]+1)
    if i%2==0:
        val.append(arr[i//2]+1)
    val.append(arr[i-1]+1)

    arr[i] = min(val)

sys.stdout.write(str(arr[num]))