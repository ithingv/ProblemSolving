#Silver 4 10816	숫자 카드 2 ESSENTIAL	

from collections import Counter

N = int(input())
card_list = list(map(int, input().split()))
card_counter = Counter(card_list)

M = int(input())
num_list = list(map(int, input().split()))
i = 0

while i < len(num_list):
    
    num = num_list[i]
    
    if num in card_counter:
        if i == len(num_list) - 1:
            print(card_counter[num])
        else:
            print(card_counter[num], end = " ")
    else:
        if i == len(num_list) - 1:
            print(0)
        else:
            print(0, end= " ")
    i += 1