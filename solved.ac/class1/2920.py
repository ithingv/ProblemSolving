import sys

arr = list(map(int, sys.stdin.readline().split()))

def main(arr):

    result = ""

    # ascending 판별
    if arr[0] == 1:
        prev_num = arr[0]
        for i in range(1,8):
            next_num = arr[i]
            if prev_num+1 != next_num:
                result += "mixed"
                print(result)
                return 
            prev_num += 1
        result += "ascending"

    # descending 판별
    elif arr[0] == 8:
        prev_num = arr[0]
        for i in range(1,8):
            next_num = arr[i]
            if prev_num-1 != next_num:
                result += "mixed"
                print(result)
                return 
            prev_num -= 1

        result += "descending"
        
    else:
        result += "mixed"

    print(result)

if __name__ == "__main__":
    main(arr)


