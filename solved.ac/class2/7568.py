#Silver 5 덩치	

N = int(input())

i = 0
person_list = []

while i < N:
    x, y = map(int, input().split())
    person_list.append((x,y))
    i += 1

j = 0
while j < N:
    curr_person = person_list[j]
    rank = 1
    for person in person_list:
        if person == curr_person:
            continue
        else:
            if curr_person[0] < person[0] and curr_person[1] < person[1]:
                rank += 1
            else:
                continue
    j += 1
    
    if j == N:
        print(rank)
        break
        
    print(rank, end = " ")