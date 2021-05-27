import sys

def isNum(s):
    try:
        int(s)
        return True
    except:
        return False

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = dict()
pokemon_name_list = []

i = 0
while i < N:
    pokemon = sys.stdin.readline().strip()
    pokemon_name_list.append(pokemon)
    pokemon_dict[pokemon] = i + 1
    i += 1

j = 0
while j < M:
    q = sys.stdin.readline().strip()
    if isNum(q):
        q = int(q)
        answer = pokemon_name_list[q-1]
    else:
        answer = pokemon_dict[q]
    
    print(answer)
    j += 1