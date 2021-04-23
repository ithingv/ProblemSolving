H, M = map(int, input().split())
if (H >= 0 and H <= 23) and (M >= 0 and M <= 59):
    if M - 45 >= 0:
        M -= 45
    elif M - 45 < 0:
        if H == 0:
            H = 23
            M += 15
        else:
            H -= 1
            M += 15
print(H, M)