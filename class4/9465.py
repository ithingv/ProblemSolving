import sys

num = int(sys.stdin.readline())
result=''

for i in range(num):
    
    size = int(sys.stdin.readline())
    arr = [ [0]*2 for i in range(size)]
    
    line = sys.stdin.readline().rstrip()
    line += ' ' + sys.stdin.readline().rstrip()
    
    for (j,e) in enumerate(line.split()):
        arr[j%size][j//size] = int(e)
    
    T = [ [0] *3 for i in range(size)]
    
    T[0][0] = 0
    T[0][1] = arr[0][0]
    T[0][2] = arr[0][1]
    
    for j in range(1,size):
        T[j][0] = 0 + max(T[j-1])
        T[j][1] = 0 + max(T[j-1][0], T[j-1][2]) + arr[j][0]
        T[j][2] = 0 + max(T[j-1][0], T[j-1][1]) + arr[j][1]
    
    result += str(max(T[size-1])) + '\n'
    
sys.stdout.write(result)
      