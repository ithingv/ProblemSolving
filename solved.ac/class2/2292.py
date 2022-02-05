# 브론즈 2 벌집

def shortest_dist(num):
    curr_val = 2
    res = 0
    while True:
        if curr_val > num:
            print(res + 1)
            break
        res += 1
        curr_val += 6 * res
        
num = int(input())
shortest_dist(num)