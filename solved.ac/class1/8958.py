N = int(input())
i = 0
while i < N:
    ox = list(input())
    ox_sum = 0
    acc = 0
    j = 0
    while j < len(ox):
        if ox[j] == 'O':
            acc += 1
            ox_sum += acc
        elif ox[j] == 'X':
            acc = 0
            ox_sum += acc
        j += 1
    print(ox_sum)
    i += 1