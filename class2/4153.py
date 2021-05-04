while True:
    
    arr = list(map(int, input().split()))    
    arr.sort()
    
    x, y, z = arr[0], arr[1], arr[2]
    if x == 0 and y == 0 and z == 0:
        break
    print("right") if x*x + y*y == z*z else print("wrong")