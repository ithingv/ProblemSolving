res = int(input())

if res >= 90 and res <= 100:
    print('A')
elif res >= 80 and res < 90:
    print('B')
elif res >= 70 and res < 80:
    print('C')
elif res >= 60 and res < 70:
    print('D')
else:
    print('F')