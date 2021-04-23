res_dict = dict()
i = 0
while i < 10:
    curr = int(input()) % 42
    if curr not in res_dict:
        res_dict[curr] = 0
    else:
        res_dict[curr] += 1
    i+= 1

res = [num for num in res_dict.keys()]
print(len(res))