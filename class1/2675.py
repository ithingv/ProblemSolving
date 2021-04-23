N = int(input())
i = 0
while i < N:
    r, word = map(str, input().split())
    r = int(r)
    j = 0
    while j < len(word):
        k = 0
        while k < r:
            print(word[j], end = '')
            k += 1
        j+= 1
    i += 1
    print()